import turtle
for x in range(10):
	turtle.forward(x*10)
	turtle.left(90)
	

import turtle
colors=["blue", "red", "green", "pink", "orange", "purple", "yellow"]

t= turtle.Pen()
turtle.bgcolor("black")

for x in range(360):
	t.pencolor(colors[x%7])
	t.width(x/10 +1)
	t.forward(x*2)
	t.left(90)

import turtle

p= turtle.Turtle()
p.color("blue")
def func(size):
	for x in range(14):
		p.fd(size)
		p.left(90)
		size=size+15
func(6)
func(36)
func(42)
func(56)

