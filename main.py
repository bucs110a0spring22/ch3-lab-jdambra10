import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo_distance = random.randrange(1,100)
leonardo_distance = random.randrange(1,100)
michelangelo.forward(michelangelo_distance)
leonardo.forward(leonardo_distance)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

max_laps = 20
for lap in range(max_laps):
  michelangelo.forward(random.randrange(1,10))
  leonardo.forward(random.randrange(1,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
leonardo.down()
triangle = 3
square = 4
hexagon = 6
nonagon = 9
dodecagon = 12

def drawShape(shape):
  for side in range(shape):
    leonardo.forward(50)
    leonardo.right(360/shape)
    if side == shape-1:
      leonardo.clear()

drawShape(triangle)
drawShape(square)
drawShape(hexagon)
drawShape(nonagon)
drawShape(dodecagon)

window.exitonclick()
