import turtle
import numpy as np

hr = turtle.Turtle()
hr.speed("fastest")

def cardioid(val,points,num,c=0,d=0):
    hr.penup()
    hr.sety(-280)
    hr.pendown()
    hr.circle(val)
    for a in range(1,points+1): 
        counter= 2*np.pi/points
        counter_2 = num*counter
        point1_x = (val)*np.cos(c) 
        point1_y = (val)*(1+np.sin(c)) 
        point2_x = (val)*np.cos(d) 
        point2_y = (val)*(1+np.sin(d))
        hr.speed("fastest")
        hr.pen(pencolor="gray")
        hr.penup()
        hr.goto((point1_x,point1_y-280)) 
        hr.pendown()
        hr.goto(point2_x,point2_y-280) 
        c+=counter
        d+=counter_2


for a in range(2,30):
    cardioid(280,200,a)
    hr.end_fill()
    hr.reset()
#cardioid(130,300,30)
#hr.done()
