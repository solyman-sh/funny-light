from turtle import *
import colorsys
bgcolor("Black")
tracer(50)
h = .04
for i in range(200):
    c= colorsys.hsv_to_rgb(h,1,1)
    h+=0.005
    width(i//100+1)
    pencolor(c)
    fillcolor(c)
    left(59)
    begin_fill()
    forward(i*0.5)
    circle(i*0.3)
    end_fill()
    right(90)
    forward(i*1.5)
    circle(i,90)
done()