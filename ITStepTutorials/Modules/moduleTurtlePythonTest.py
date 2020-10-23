import turtle
'''
Turtle module for drawing objects in canvas
> pip install PythonTurtle
'''

t = turtle.Pen()
colors = ['red', 'green', 'blue', 'yellow', 'purple']
for i in range(90):
    t.pencolor(colors[i % 5])
    t.width(i / 10)
    t.forward(i)
    t.left(60)