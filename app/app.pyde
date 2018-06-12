add_library('controlP5')
# Page 0 = Menu Page
# Page 1 = Chase the Number Instruction Page
# Page 2 = Number Detective Instruction Page
# Page 3 = Game 3 Instruction Page
# Page 4 = Game 4 Instruction Page
# Page 5 = Chase the Number Game Page
# Page 6 = Number Detective Game Page
# Page 7 = Game 3 Game Page
# Page 8 = Game 4 Game Page
# Page 9 = Scoreboard Page
import random
pagenumber = 0
resetgame = 0
t = 0
o = 0

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
        displaytext("Extra Bold",255,self.textsize,self.buttontext,self.x+(self.buttonwidth/2),self.y+(self.buttonlength/2)+(self.buttonlength/8))
    def press(self):
        if self.x<mouseX<self.x+self.buttonwidth and self.y<mouseY<self.y+self.buttonlength:
            return True
        else:
            return False


### START - HOME PAGE ###
chasing = Button(50,150,'Large','Chase The Numbers')
number = Button(400,150,'Large','Number Detective') 
game3 = Button(50,250,'Large','Game 3')
game4 = Button(400,250,'Large','Game 4')
### END - HOME PAGE ##

### START - INSTRUCTION PAGE ###
gamestart = Button(25,425,'Large','Start Game')
viewboard = Button(425,425,'Large','View Scoreboard')
returnmenu = Button(288,425,'Small','Menu')
### END - INSTRUCTION PAGE ##

exitgame = Button(25,425,'Large','Exit Game')
savescore = Button(425,425,'Large','Save Score')

### START - NUMBER DETECTIVE PAGE ###
easybutton = Button(75,350,'Small','3 Digit')
medbutton = Button(275,350,'Small','4 Digit')
hardbutton = Button(475,350,'Small','5 Digit')
newmenu = Button(50,425,'Large','Menu')
newviewboard = Button(400,425,'Large','View Scoreboard')
### END - NUMBER DETECTIVE PAGE ###

submit = Button(550,250,'Small','Submit')
submit_guess = Button(500,270,'Small','Submit')


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

      
    def display(self):
        self.game = 0
        i = 0
        if self.lowhigh == 1:
            displaytext("Extra Bold",255,35,"Select the LOWEST Number",350,50)
        if self.lowhigh == 2:
            displaytext("Extra Bold",255,35,"Select the HIGHEST Number",350,50)
        while i < len(self.posX):
            fill(255)
            ellipse(self.posX[i],self.posY[i],50,36)
            displaytext("Bold",0,20,self.number_list[i],self.posX[i],self.posY[i]+8)
            i += 1

        scoretext = "Score: "+str(self.score)
        if len(number_scorelist) == 0:
            highscore = 0
        else:
            highscore = number_scorelist[0]
        highscoretext = "High Score: "+str(highscore)
        displaytext("Extra Bold",255,25,scoretext,100,450)
        displaytext("Extra Bold",255,25,highscoretext,100,475)
        
    def gameover(self):
        self.game = 1
        self.posX = []
        self.posY = []
        self.number_list = []
        displaytext("Extra Bold",255,50,"Game Over!",350,250)
        global resetgame
        resetgame = 1
        exitgame.create()
        savescore.create()
        return int(self.score)
            
    def remove_bubble(self,index):
        self.posX.remove(self.posX[index])
        self.posY.remove(self.posY[index])
        self.number_list.remove(self.number_list[index])

            
    def press(self):
        OpenSansExtraBold = loadFont("OpenSans-Extrabold-48.vlw")
        if self.game == 0:
            i = 0
            if self.lowhigh == 1:
                numbertarget = min(self.number_list)
            if self.lowhigh == 2:
                numbertarget = max(self.number_list)
            while i < len(self.posX):
                if len(self.posX) == 1:
                    fill(0,255,0)
                    textFont(OpenSansExtraBold,25)
                    textAlign(CENTER)
                    text("+1",100,425)
                    self.gen_bubble()
                    self.score += 1
                    break
                if mouseX in range(self.posX[i]-25,self.posX[i]+25):
                    if mouseY in range(self.posY[i]-18,self.posY[i]+18):
                        if numbertarget == self.number_list[i]:
                            fill(0,255,0)
                            textFont(OpenSansExtraBold,25)
                            textAlign(CENTER)
                            text("+1",100,425)
                            self.remove_bubble(i)
                            self.score += 1
                            self.lowhigh = random.randint(1,2)
                        elif self.score != 0:
                            fill(124,10,2)
                            textFont(OpenSansExtraBold,25)
                            textAlign(CENTER)
                            text("-2",100,425)
                            self.score -= 1
                            
                i += 1
        if self.game == 1:
            if exitgame.press() == True:
                global pagenumber
                pagenumber = 0
            if savescore.press() == True:
                global pagenumber
                pagenumber = 9
                global scoresub
                scoresub = 1
                global gamename
                gamename = "Chase the Number"

       
                
                
                
class Timer():
    def __init__(self,sec):
        self.sec = sec
        self.starttimer = millis()
        
    def update(self):
        timetext = "Time Left: "+str(self.sec)
        displaytext("Extra Bold",255,35,timetext,550,475)
        
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
chasetimer = Timer(60)

def startup():
    global gamebubble
    gamebubble = NumberBubble()
    global chasetimer
    chasetimer = Timer(60)
    
def displaytext(font,fontfill,fontsize,inputtext,posX,posY):
    if font == "Extra Bold":
        OpenSansExtraBold = loadFont("OpenSans-Extrabold-48.vlw")
        textFont(OpenSansExtraBold,fontsize)
    if font == "Bold":
        OpenSansBold = loadFont("OpenSans-Bold-48.vlw")
        textFont(OpenSansBold,fontsize)
    if font == "Regular":
        OpenSansRegular = loadFont("OpenSans-48.vlw")
        textFont(OpenSansRegular,fontsize)
    fill(fontfill)
    textAlign(CENTER)
    text(inputtext,posX,posY)
    
    
def setup():
    size(700,500)
    background(91,94,125)
    
    ### DOWNLOAD SCORES##
    with open ("numberscore.txt") as number_score:
        i = 0
        global number_namelist
        number_namelist = []
        global number_scorelist
        number_scorelist = []
        lines = [x.replace('\n', '') for x in number_score.readlines()]
        while i != len(lines):
            number_namelist.append(lines[i])
            number_scorelist.append(int(lines[i+1]))
            i += 2
    
def draw():
    global pagenumber
    background(91,94,125)
    
    def instructp(title,instructiontext): # Create instruction page
        displaytext("Extra Bold",255,50,title,350,75)
        gamestart.create()
        viewboard.create()
        returnmenu.create()
        displaytext("Regular",255,24,instructiontext,350,115)
    
    if pagenumber == 0: # Set Up Home Page
        global resetgame
        if resetgame == 1:
            startup()
            resetgame = 0
            timerset = 0
        displaytext("Extra Bold",255,50,"Math Games!",350,75)
        chasing.create()
        number.create()
        game3.create()
        game4.create()
        
    if pagenumber == 1: # Set Up Chase the Numbers Page
        instructp("Chase The Numbers","INSTRUCTIONS:\n"
                  "- You will be asked to find the lowest or highest number in\na set of 10 numbers and destory it.\n"
                  "- You EARN 1 point for every number destroyed.\n"
                  "- Select the wrong number and LOSE 1 point.\n"
                  "- Clear the board as fast as possible to be presented with\n another set of 10 numbers.\n"
                  "- Beware! You only have 60 seconds to earn as many points \nas possible.\n"
                  "- Watch for GREEN blocks to add time to the clock.")
    
    if pagenumber == 2: # Set Up Divisor Snake
        displaytext("Extra Bold",255,50,"Number Detective",350,75)
        easybutton.create()
        medbutton.create()
        hardbutton.create()
        newviewboard.create()
        newmenu.create()
        displaytext("Regular",255,24,"INSTRUCTIONS:\n"
                  "- You've been given the job of cracking a secret code in the\nleast amount of tries.\n"
                  "- Once you make a guess of what the secret code is you'll be\ntold whether it's too high or too low.\n"
                  "- You'll also be told how many digits in the code you got\ncorrect, but won't know the positions.\n"
                  "Select your difficulty:",350,115)
        
    if pagenumber == 5: # Chase the Number Game Screen
        
        if chasetimer.timecheck() == True:
            gamebubble.display()
            chasetimer.update()
            
        else:
            global gamescore
            gamescore = gamebubble.gameover()
            
    if pagenumber == 6: #Number Detective Screen
        if dif == 1:
            displaytext("Extra Bold",255,30,"Crack the code! You need to guess\nwhat the 3 digits of the code are...",350,50)
            leng = 3
        if dif == 2:
            displaytext("Extra Bold",255,30,"Crack the code! You need to guess\nwhat the 4 digits of the code are...",350,50)
            leng = 4
        if dif == 3:
            displaytext("Extra Bold",255,30,"Crack the code! You need to guess\nwhat the 5 digits of the code are...",350,50)
            leng = 5
        displaytext("Extra Bold",255,25,"Enter your guess:",175,305)
        global o
        if o == 0:
                font = createFont("OpenSansBold", 35)
                global cp5
                cp5 = ControlP5(this)
                cp5.addTextfield("").setPosition(325,250).setSize(
                120,100).setFont(font).setFocus(True).setColor(color(255)).setAutoClear(False).setInputFilter(ControlP5.INTEGER)
                o = 1
        if len(cp5.get(Textfield, "").getText()) > leng:
                inputtext = str(cp5.get(Textfield, "").getText())
                font = createFont("OpenSansBold", 35)
                cp5.addTextfield("").setText(inputtext[:leng]).setPosition(325,250).setSize(
                120,100).setFont(font).setFocus(True).setColor(color(255)).setAutoClear(False).setInputFilter(ControlP5.INTEGER)
        submit_guess.create()
                
            
    if pagenumber == 9: #Scoreboard Screen
        
        if scoresub == 1:
            displaytext("Extra Bold",255,40,"Score Submission",350,50)
            scoretxt = "Your Score: "+str(gamescore)
            displaytext("Extra Bold",255,30,scoretxt,350,200)
            displaytext("Extra Bold",255,25,"Name:",100,290)
            global t
            if t == 0:
                font = createFont("OpenSansBold", 20)
                global cp5
                cp5 = ControlP5(this)
                cp5.addTextfield("").setPosition(175,250).setSize(
                350,60).setFont(font).setFocus(True).setColor(color(255)).setAutoClear(False)
                t = 1
            submit.create()
            
        if scoresub == 2:
            cp5.get("").hide()
            displaytext("Extra Bold",255,40,"Score Submitted!",350,410)
            
        if scoresub == 2 or scoresub == 3:
            headline = "Scoreboard - "+gamename
            displaytext("Extra Bold",255,40,headline,350,50)
            fill(255,0,0,0)
            strokeWeight(3)
            rect(10,65,680,300)
            scoreboard_text = ""
            if gamename == "Chase the Number":
                i = 0
                while i < len(number_namelist) and i < 5:
                        scoreboard_text += "\n"+number_namelist[i]+" - "+"Score: "+str(number_scorelist[i])+"\n"
                        i += 1
                displaytext("Regular",255,24,scoreboard_text,350,70)
            strokeWeight(1)
            returnmenu.create()
                

def mouseClicked():
    global pagenumber
    if pagenumber == 0: # Home Page Buttons
        if chasing.press() == True:
            pagenumber = 1
        if number.press() == True:
            pagenumber = 2
    if pagenumber == 1: # Chase the Numbers Instruction Buttons
        if gamestart.press() == True:
            pagenumber = 5
        if viewboard.press() == True:
            pagenumber = 9
            global gamename
            gamename = "Chase the Number"
            global scoresub
            scoresub = 3
        if returnmenu.press() == True:
            pagenumber = 0
    if pagenumber == 2: # Number Detective Instruction Buttons
        if easybutton.press() == True:
            pagenumber = 6
            global dif
            global digit
            dif = 1
            digit = random.randint(100,999)
        if medbutton.press() == True:
            pagenumber = 6
            global dif
            global digit
            dif = 2
            digit = random.randint(1000,9999)
        if hardbutton.press() == True:
            pagenumber = 6
            global dif
            global digit
            dif = 3
            digit = random.randint(10000,99999)
        if newviewboard.press() == True:
            pagenumber = 9
        if newmenu.press() == True:
            pagenumber = 0 
    
    if pagenumber == 5:
        gamebubble.press()
        
    if pagenumber == 6:
        if submit_guess.press() == True and digit != int(cp5.get(Textfield, "").getText()):
            print(digit)
            
    if pagenumber == 9:
        if scoresub == 1 and submit.press() == True and cp5.get(Textfield, "").getText() != "":
            global scoresub
            scoresub = 2
            global t
            t = 0
            global number_namelist
            number_namelist.append(str(cp5.get(Textfield, "").getText()))
            global number_scorelist
            number_scorelist.append(int(gamescore))
            sortedscore = sorted(number_scorelist, reverse= True)
            new_namelist = []
            for s in sortedscore:
                    indx = number_scorelist.index(s)
                    new_namelist.append(number_namelist[indx])
            number_namelist = new_namelist
            number_scorelist = sorted(number_scorelist, reverse= True)
            with open ("numberscore.txt", "w") as number_score:
                i = 0
                while i < len(number_namelist):
                    number_score.write(str(number_namelist[i])+'\n')
                    number_score.write(str(number_scorelist[i])+'\n')
                    i += 1
        if scoresub != 1 and returnmenu.press() == True:
            pagenumber = 0
            
