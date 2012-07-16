class color:
    def SetInfo(self,red,green,blue):
        self.Red=red
        self.Green=green
        self.Blue=blue
    def show(self):
        print("color1: %s"%(self.Red))
        print("color2: %s"%(self.Green))
        print("color3: %s"%(self.Blue))

ListOfColors=[]
ColorInfo=color()
ColorInfo.SetInfo("red","green","blue")
ListOfColors.append(ColorInfo)

class saturation(color):
    pass

class Hue(color):
    pass

for color in ListOfColors:
    ColorInfo.show()
    
