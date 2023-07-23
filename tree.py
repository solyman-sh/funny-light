from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(5)
h=0.74
lt(90)
def tree(x):
    global h
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    if (x<10):
        return
    else:
        fd(x)
        lt(30)
        tree(3*x/4)
        rt(60)
        tree(3*x/4)
        lt(30)
        bk(x)
tree(70)
done()