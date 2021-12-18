import turtle
import math
t = turtle.Turtle()
def s(n, l):

    if n == 0: # stop conditions

        # draw filled rectangle

        t.color('black')
        t.begin_fill()
        for _ in range (4):
            t.forward(l)
            t.left(90)
        t.end_fill()

    else: # recursion

        # around center point create 8 smalles rectangles.
        # create two rectangles on every side 
        # so you have to repeat it four times

        for _ in range(4):
            # first rectangle
            s(n-1, l/3)    
            t.forward(l/3)

            # second rectangle
            s(n-1, l/3)    
            t.forward(l/3)

            # go to next corner
            t.forward(l/3)
            t.left(90)

        # update screen
        t.update()

# --- main ---    

# stop updating screen (to make it faster)
t.tracer(0) 

# start
try:
  s(4, 400)
except:
  print("This loop has reached it's max callback")
# event loop 
t.done()