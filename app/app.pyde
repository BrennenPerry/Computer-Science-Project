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
import random
pagenumber = 0
resetgame = 0

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
### END - INSTRUCTION PAGE ##

exitgame = Button(25,425,'Large','Exit Game')

class NumberBubble():

    def __init__(self):
        self.gen_bubble()
        self.score = 0
        self.game = 0
                
    def gen_bubble(self):
        self.posX = [random.randint(25,670)]
        self.posY = [random.randint(75,400)]
        self.lowhigh = random.randint(1,2) # To determine if user should select the lowest or highest number (1 = Lowest, 2 = Highest)
        p = 1
        while p != 10: # Generate a list of 10 x and y pos.
            x = random.randint(25,670)
            y = random.randint(75,400)
            check = False
            for l in self.posX:
                for j in self.posY:
                    if x in range(l-51,l+51) and y in range(j-37,j+37):
                        check = True
                        break
                if check == True:
                    break
            if check == False:
                self.posX.append(x)
                self.posY.append(y)
                p += 1

        self.number_list = [random.randint(1,99)]
        n = 1
        while n != 10: # Generate a list of 10 random int 
            num = random.randint(1,99)
            check = False
            for t in self.number_list:
                if num == t:
                    check = True

            if check == False:
                self.number_list.append(num)
                n += 1
                
        print(self.posX)

      
    def display(self):
        self.game = 0
        i = 0            
        OpenSansExtraBold = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSansExtraBold,35)
        textAlign(CENTER)
        if self.lowhigh == 1:
            text("Select the LOWEST Number",350,50)
        if self.lowhigh == 2:
            text("Select the HIGHEST Number",350,50)
        while i < len(self.posX):
            fill(255)
            ellipse(self.posX[i],self.posY[i],50,36)                
            OpenSansBold = loadFont("OpenSans-Bold-48.vlw")
            fill(0)
            textFont(OpenSansBold,20)
            textAlign(CENTER)
            text(self.number_list[i],self.posX[i],self.posY[i]+8)
            i += 1
    
        OpenSansExtraBold = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSansExtraBold,25)
        textAlign(CENTER)
        scoretext = "Score: "+str(self.score)
        text(scoretext,100,450)
        
    def gameover(self):
        self.game = 1
        self.posX = []
        self.posY = []
        self.number_list = []
        OpenSansExtraBold = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSansExtraBold,50)
        textAlign(CENTER)
        text("Game Over!",350,250)
        global resetgame
        resetgame = 1
        exitgame.create()
            
    def remove_bubble(self,index):
        self.posX.remove(self.posX[index])
        self.posY.remove(self.posY[index])
        self.number_list.remove(self.number_list[index])

            
    def press(self):
        if self.game == 0:
            i = 0
            if self.lowhigh == 1:
                numbertarget = min(self.number_list)
            if self.lowhigh == 2:
                numbertarget = max(self.number_list)
            while i < len(self.posX):
                if len(self.posX) == 1:
                    self.gen_bubble()
                    self.score += 1
                    break
                if mouseX in range(self.posX[i]-25,self.posX[i]+25):
                    if mouseY in range(self.posY[i]-18,self.posY[i]+18):
                        if numbertarget == self.number_list[i]:
                            self.remove_bubble(i)
                            self.score += 1
                            self.lowhigh = random.randint(1,2)
                i += 1
        if self.game == 1:
            if exitgame.press() == True:
                global pagenumber
                pagenumber = 0
class Snake():
    
    def __init__(self):
        self.gen_food()
        self.score = 0
        self.game = 0

    def gen_food(self):
        self.posX = [random.randint(25,670)]
        self.posY = [random.randint(75,400)]
        p = 1
        while p != 5:
            x = random.randint(25,670)
            y = random.randint(75,400)
            check = False
            for l in self.posX:
                for j in self.posY:
                    if x in range(l-51,l+51) and y in range(j-37,j+37):
                        check = True
                        break
                if check == True:
                    break
            if check == False:
                self.posX.append(x)
                self.posY.append(y)
                p += 1
        
        self.number_list = [random.randint(1,99)]
        n = 1
        while n != 5:
            num = random.randint(1,99)
            check = False
            for t in self.number_list:
                if num == t:
                    check = True
                
            if check == False:
                self.number_list.append(num)
                n += 1
        print (self.posX)
    def display(self):
        self.game = 0
        i = 0
        while i < len(self.posX):
            fill(211,111,95)
            rect(self.posX[i],self.posY[i],25,25)
            OpenSansBold = loadFont("OpenSans-Bold-48.vlw")  
            fill(0)
            textFont(OpenSansBold,20)
            textAlign(CENTER)
            text(self.number_list[i],self.posX[i],self.posY[i])
            i += 1

class Timer():
    def __init__(self,sec):
        self.sec = sec
        self.starttimer = millis()
        
    def update(self):
        OpenSansExtraBold = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSansExtraBold,35)
        textAlign(CENTER)
        timetext = "Time Left: "+str(self.sec)
        text(timetext,550,475)
        
        timedif = millis() - self.starttimer
        
        if timedif >= 1000:
            self.sec -= 1
            self.starttimer = millis()
    
        
    def timecheck(self):
        if self.sec >= 0:
            return True
        else:
            return False
            
            
gamebubble = NumberBubble()
gamesnake = Snake()
chasetimer = Timer(60)
snaketimer = Timer(120)

def startup():
    global gamebubble
    gamebubble = NumberBubble()
    global gamesnake
    gamesnake = Snake()
    global chasetimer
    chasetimer = Timer(60)
    global snaketimer
    snaketimer = Timer(120)
    
def setup():
    size(700,500)
    background(91,94,125)
    
def draw():
    global pagenumber
    background(91,94,125)
    
    def instructp(title,instructiontext): # Create instruction page
        OpenSansBold = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSansBold,50)
        textAlign(CENTER)
        text(title,350,75)
        gamestart.create()
        viewboard.create()
        returnmenu.create()
        OpenSansRegular = loadFont("OpenSans-48.vlw")
        textFont(OpenSansRegular,24)
        textAlign(CENTER)
        text(instructiontext,350,115)
    
    if pagenumber == 0: # Set Up Home Page
        global resetgame
        if resetgame == 1:
            startup()
            resetgame = 0
            timerset = 0
        OpenSansBold = loadFont("OpenSans-Extrabold-48.vlw")
        fill(255)
        textFont(OpenSansBold,50)
        textAlign(CENTER)
        text("Math Games!",350,75)
        chasing.create()
        divisor.create()
        game3.create()
        game4.create()
        game5.create()
        game6.create()
        
    if pagenumber == 1: # Set Up Chase the Numbers Page
        instructp("Chase The Numbers","INSTRUCTIONS:\n"
                  "- You will be asked to find the lowest or highest number in\na set of 10 numbers and destory it.\n"
                  "- You EARN 1 point for every number destroyed.\n"
                  "- Select the wrong number and LOSE 2 points.\n"
                  "- Clear the board as fast as possible to be presented with\n another set of 10 numbers.\n"
                  "- Beware! You only have 60 seconds to earn as many points \nas possible.\n"
                  "- Watch for GREEN blocks to add time to the clock.")
    
    if pagenumber == 2: # Set Up Divisor Snake
        instructp("Divisor Snake","INSTRUCTIONS:\n"
                  "- Your job is to guide a snake around the game board with\nyour keyboard arrows while keeping it well fed.\n"
                  "- The snake eats divisors for a specific number that will\nchange after each time it eats.\n"
                  "- Be quick! The food may expire and disappear at any time.\n"
                  "- Should you try to feed it a number that isn't a divisor for\nthe specific number you will be given a STRIKE.\n"
                  "- Get 3 STRIKES and your snake dies!\n"
                  "- You have 120 seconds to eat as many divisors as possible." )
        
    if pagenumber == 7: # Chase the Number Game Screen
        
        if chasetimer.timecheck() == True:
            gamebubble.display()
            chasetimer.update()
            
        else:
            gamebubble.gameover()
    
    if pagenumber == 8:# Snake game
        
        if snaketimer.timecheck() == True:
            gamesnake.display()
            snaketimer.update()
            
        #else:
           #gamesnake.gameover()
    
    
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
    if pagenumber == 2: # Divisor Instruction Buttons
        if gamestart.press() == True:
            pagenumber = 8
        if viewboard.press() == True:
            pagenumber = 13
        if returnmenu.press() == True:
            pagenumber = 0
    if pagenumber == 7:
        gamebubble.press()
        
               
    
