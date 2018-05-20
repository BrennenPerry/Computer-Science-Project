pagenumber = 0

class Button():
    def __init__(self,xPos,yPos,buttonsize,buttontext):
        self.x = xPos
        self.y = yPos
        self.buttontext = buttontext
        if buttonsize == 'Small':
            self.buttonwidth = 200
            self.buttonlength = 50
            self.textsize = 15
            
        if buttonsize == 'Large':
            self.buttonwidth = 250
            self.buttonlength = 60
            self.textsize = 20
            
    def create(self):
        fill(255,0,180)
        rect(self.x,self.y,self.buttonwidth,self.buttonlength)
        fill(255)
        OpenSans = loadFont("OpenSans-Extrabold-48.vlw")
        textFont(OpenSans,self.textsize)
        textAlign(CENTER)
        text(self.buttontext,self.x+(self.buttonwidth/2),self.y+(self.buttonlength/2)+(self.buttonlength/8))
        
    def press(self):
        if self.x<mouseX<self.x+self.buttonwidth and self.y<mouseY<self.y+self.buttonlength:
            return True
        else:
            return False

### START - HOME PAGE ###
chasing = Button(25,150,'Large','Chase The Numbers')
divisor = Button(325,150,'Large','Divisor Snake') 
game3 = Button(25,250,'Large','Game 3')
game4 = Button(325,250,'Large','Game 4') 

buttonlist = [chasing,divisor,game3,game4]
### END - HOME PAGE ##

def setup():
    size(600,400)
    background(91,94,125)
    
def draw():
    global pagenumber
    background(91,94,125)
    
    if pagenumber == 0: # Set Up Home Page
        OpenSans = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSans,40)
        textAlign(CENTER)
        text("Math Games!",300,100)
        for item in buttonlist:
            item.create()
            
def mouseClicked():
    global pagenumber
    if pagenumber == 0: # Home Pgae Buttons
        if chasing.press() == True:
            pagenumber = 1
        if divisor.press() == True:
            pagenumber = 2
