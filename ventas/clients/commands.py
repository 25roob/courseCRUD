import click


@click.group()
def clients():
    """Manages the clients lifecycle"""


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""


@clients.command()
@click.pass_context
def ulist(ctx):
    """List all clients"""


@clients.command()
@click.pass_context
def updated(ctx, client_uid):
    """Updates a client"""


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""


all = clients
