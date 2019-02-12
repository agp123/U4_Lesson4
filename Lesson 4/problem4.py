from turtle import *

mia = Turtle()

mia.color('blue')
mia.pensize(6)
mia.speed(8)
mia.shape('turtle')

vale = Turtle()

vale.color('purple')
vale.pensize(6)
vale.speed(8)
vale.shape('turtle')

for x in range(3):
	mia.forward(150)
	mia.left(120)

vale.circle(100)




mainloop()