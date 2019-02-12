from turtle import *

mia = Turtle()

mia.color('black')
mia.pensize(5)
mia.speed(10)
mia.shape('turtle')

for x in range(4):
	mia.forward(150)
	mia.left(90)

mainloop()