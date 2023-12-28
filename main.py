import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    
        self.turtle = t.Turtle()
    
    def showdisk(self):
        self.turtle.forward(self.dwidth/2)
        self.turtle.left(90)
        self.turtle.forward(self.dheight)
        self.turtle.left(90)
        self.turtle.forward(self.dwidth)
        self.turtle.left(90)
        self.turtle.forward(self.dheight)
        self.turtle.left(90)
        self.turtle.forward(self.dwidth/2)
        
    def newpos(self, xpos, ypos):
        self.turtle.goto(xpos, ypos)
        
    def cleardisk(self):
        self.turtle.clear()
