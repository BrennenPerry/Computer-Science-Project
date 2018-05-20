# Page 0 = Menu Page
# Page 1 = Chase the Number Instruction Page
# Page 2 = Divisor Snake Instruction Page
# Page 3 = Game 3 Instruction Page
# Page 4 = Game 4 Instruction Page
# Page 5 = Game 5 Instruction Page
# Page 6 = Game 6 Instruction Page
# Page 7 Chase the Number Game Page
# Page 8 = Divisor Snake Game Page
# Page 9 = Game 3 Game Page
# Page 10 = Game 4 Game Page
# Page 11 = Game 5 Game Page
# Page 12 = Game 6 Game Page
# Page 13 = Scoreboard Page

pagenumber = 0

class Button():
    def __init__(self,xPos,yPos,buttonsize,buttontext):
        self.x = xPos
        self.y = yPos
        self.buttontext = buttontext
        if buttonsize == 'Small':
            self.buttonwidth = 125
            self.buttonlength = 60
            self.textsize = 20
            
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
chasing = Button(50,150,'Large','Chase The Numbers')
divisor = Button(400,150,'Large','Divisor Snake') 
game3 = Button(50,250,'Large','Game 3')
game4 = Button(400,250,'Large','Game 4')
game5 = Button(50,350,'Large','Game 5')
game6 = Button(400,350,'Large','Game 6')
### END - HOME PAGE ##

### START - INSTRUCTION PAGE ###
gamestart = Button(25,425,'Large','Start Game')
viewboard = Button(425,425,'Large','View Scoreboard')
returnmenu = Button(288,425,'Small','Menu')

def setup():
    size(700,500)
    background(91,94,125)
    
def draw():
    global pagenumber
    background(91,94,125)
    
    if pagenumber == 0: # Set Up Home Page
        OpenSans = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSans,50)
        textAlign(CENTER)
        text("Math Games!",350,75)
        chasing.create()
        divisor.create()
        game3.create()
        game4.create()
        game5.create()
        game6.create()
        
    if pagenumber == 1: # Set Up Chase the Numbers Page
        OpenSans = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSans,50)
        textAlign(CENTER)
        text("Chase the Numbers",350,75)
        gamestart.create()
        viewboard.create()
        returnmenu.create()
            
def mouseClicked():
    global pagenumber
    if pagenumber == 0: # Home Page Buttons
        if chasing.press() == True:
            pagenumber = 1
        if divisor.press() == True:
            pagenumber = 2
    if pagenumber == 1: # Chase the Numbers Instruction Buttons
        if gamestart.press() == True:
            pagenumber = 7
        if viewboard.press() == True:
            pagenumber = 13
        if returnmenu.press() == True:
            pagenumber = 0
