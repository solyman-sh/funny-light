from turtle import *
import colorsys
tracer(100)
bgcolor('black')
h=0.2
def enjoy():
    global h
    for i in range(4):
        c=colorsys.hsv_to_rgb(h,1,1)
        fillcolor(c)
        h+=0.004
        begin_fill()
        fd(50)
        rt(20)
        fd(40)
        rt(9)
        end_fill()

for j in range(1000):
    enjoy()
    goto(0,0)
    rt(1)
done()