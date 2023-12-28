import turtle as t

class Pole(object):
    def __init__(self, name="",xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        t.penup()
        t.goto(self.pxpos,self.pypos)
        t.pendown()
        for i in range(2):
            t.forward(self.pthick)
            t.left(90)
            t.forward(self.plength)
            t.left(90)
        t.penup()
    
    def pushdisk(self,disk):
        disk.showdisk()
        self.stack.append(disk)
        self.toppos += 1

    def popdisk(self):
        self.toppos -= 1
        disk = self.stack.pop()
        disk.cleardisk()
        
