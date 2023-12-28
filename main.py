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
        return disk
        
class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*150,20,(n-i)*30))
            
    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)
        
    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)
        
    def solve(self):
        self.move_tower(3,self.startp, self.destinationp,self.workspacep)
        
h = Hanoi()
h.solve()
