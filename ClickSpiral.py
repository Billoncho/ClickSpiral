# ClickSpiral.py
# Billy Ridgeway
# Generates random sized and colored square winding spirals at random
# locations on the user's screen.

import random               # Imports the random library.
import turtle               # Imports the turtle library.
t = turtle.Pen()            # Creates a new turtle pen called t.
t.speed(0)                  # Sets the pen's speed to fast.
turtle.bgcolor("black")     # Sets the background to black.

# Creates a list of colors.
colors = ["red", "yellow", "blue", "green", "orange",
          "purple", "white", "gray"]

# Define a function to draw random spirals of random sizes and colors at random locations.
def spiral(x,y):
    t.pencolor(random.choice(colors))       # Pick a random color.
    size = random.randint(10,40)            # Pick a random spiral size.
    t.penup()               # Stops the pen from drawing while we change positions on the screen.
    t.setpos(x,y)           # Sets the x and y positions on the screen to those generated
                            # by the for loop.
    t.pendown()             # Sets the pen so it can draw.
    for m in range(size):   # Sets the range of m to the value contained in the variable size.
        t.forward(m*2)      # Moves the pen forward by the value contained in m times 2.
        t.left(91)          # Moves the pen left by 91 degrees.

turtle.onscreenclick(spiral)    # Calls the spiral function when the screen
                                # is clicked.
    
    
    
