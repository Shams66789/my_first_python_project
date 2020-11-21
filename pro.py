from tkinter import *
import math

_OuterDia = 200
_width = 800
_height = 600
_vertices = 12

def grt_coords(od, cx, cy, vertices = 3):
    angle = 2*math.pi/vertices
    return[[math.cos(angle*i)*od/2+cx, math.sin(angle*i)*od/2+cy]for i in range(0,vertices)]

draw_arc = lambda px,py,r,c,delta : Canvas.create_arc(px-r,py+r,px+r,py-r,outline=c, fill='black', style = 'arc', width=3,start = 60-delta,extent = 240)

root = Tk()
root.title("Pyometry Sadhana")
Canvas = Canvas(width = _width, height = _height,bg = 'black')

def spiral_circle(od,px,py,v):
    pt = grt_coords(od,px,py,v)
    for i,p in enumerate(pt):
        draw_arc(p[0],p[1],od/2,'red',i*360/v)

spiral_circle(_OuterDia,_width/2,_height/2,_vertices)
Canvas.pack()
mainloop()