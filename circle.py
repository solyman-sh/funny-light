from turtle import *
import colorsys
speed(0)
bgcolor("black")
h=0.08

for i in range(60):
    c= colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    fd(i)
    rt(20)
    lt(80)
    circle(150)
    fd(40)
done()