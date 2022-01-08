import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
        
    else:
        print("The client is already in the client's list")

def list_clients():
    for idx, client in enumerate(clients):
        uid = idx
        name = client['name']
        company = client['company']
        email = client['email']
        position = client['position']
        print(f'{uid} | {name} | {company} | {email} | {position}') 

def update_client(client_index, updated_client_data):
    global clients
    
    clients[client_index].update(updated_client_data)
    

def delete_client(client_index):
    global clients
    if client_index <= len(clients)-1:
        rdata = clients.pop(client_index)
    else: 
        print('Client is not in database.')
    name = rdata['name']
    company = rdata['company']
    email = rdata['email']
    position = rdata['position']
    print(f'Data deleted -> name: {name} | company: {company} | email: {email} | position: {position}') 
    

def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True
    

def _print_welcome():
    print('WELCOME TO PLATZIVENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}?: ')

    return field

def _get_client_index():
    client_index = None

    while not client_index:
        client_index = input("What's the client's uid?: ")

        if client_index == 'exit':
            client_index = None
            break
    if not client_index:
        sys.exit()

    return int(client_index)

def _new_client_data():
    return {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }

def _print_client_data(client_index):
    global clients

    data = clients[client_index]
    name = data['name']
    company = data['company']
    email = data['email']
    position = data['position']
    print(f'Client data -> name: {name} | company: {company} | email: {email} | position: {position}') 


if __name__ == '__main__':

    _initialize_clients_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _new_client_data()
        create_client(client)
        
    elif command == 'L':
        list_clients()
    elif command == 'D':
        
        client_index = _get_client_index()
        
        delete_client(client_index)
        
    elif command == 'U':
        
        client_index = _get_client_index()
        if client_index <= len(clients)-1:
            updated_client_data = _new_client_data()
            update_client(client_index, updated_client_data)
            
        else:
            print(f'The client uid: {client_index}, is not in the database.')
        
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')
        
    else:
        print('Invalid command.')

    _save_clients_to_storage()