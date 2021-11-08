import random
x1=random.randint(1,10)
y1=random.randint(1,10)
x2=random.randint(11,20)
y2=random.randint(11,20)
print(x1,y1,x2,y2)
class recGame:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def calArea(self):
        self.x_width=x2-x1
        self.y_width=y2-y1
        self.area=self.x_width*self.y_width
        print(self.area)
    def checkResult(self,user_x,user_y,user_area):#
        self.user_x=user_x
        self.user_y=user_y
        self.user_area=user_area
        if self.x1<self.user_x<self.x2 and self.y1<self.user_y<self.y2 and self.user_area==self.area:
            self.win=True
        else:
            self.win=False
    def showResult(self):
        if self.win==True:
            print("You won")
        else:
            print("You lost")
recgame=recGame(x1,y1,x2,y2)
recgame.calArea()
recgame.checkResult(int(input("Enter X pos:  ")),int(input("Enter Y pos:  ")),int(input("Enter the area of the rectangle:  ")))
recgame.showResult()