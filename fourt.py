from turtle import *
import colorsys

speed(0)
h=0.1
bgcolor("black")

for i in range(200):
    c=colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h+=0.1
    begin_fill()
    for j in range(4):
        fd(0.2*i*j)
        lt(91)
    lt(73*15/100)
    end_fill()

done()