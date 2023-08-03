from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('orange')
    circle(i)
    color('red')
    circle(i*2)
    color('white')
    circle(i*1.2)
    right(3)
    forward(3)
    
done