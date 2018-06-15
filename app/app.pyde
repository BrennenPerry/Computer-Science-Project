add_library('controlP5')
# Page 0 = Menu Page
# Page 1 = Chase the Number Instruction Page
# Page 2 = Number Detective Instruction Page
# Page 3 = Game 3 Instruction Page
# Page 4 = Chase the Number Game Page
# Page 5 = Number Detective Game Page
# Page 6 = Game 3 Game Page
# Page 7 = Scoreboard Page 

#import variables and library
import random 
pagenumber = 0
resetgame = 0 
guesscounter = 0
digitinfo = ""
t = 0
difcheck = 0

class Button(): #This creates buttons
    def __init__(self,xPos,yPos,buttonsize,buttontext):
        self.x = xPos
        self.y = yPos
        self.buttontext = buttontext
        self.textsize = 20
        if buttonsize == 'Small':
            self.buttonwidth = 125
            self.buttonlength = 60
            
        if buttonsize == 'Large':
            self.buttonwidth = 250
            self.buttonlength = 60
            
        if buttonsize == 'Extra Large':
            self.buttonwidth = 600
            self.buttonlength = 60
            
    def create(self): #Displays the button
        fill(255,0,180)
        rect(self.x,self.y,self.buttonwidth,self.buttonlength)
        displaytext("Extra Bold",255,self.textsize,self.buttontext,self.x+(self.buttonwidth/2),self.y+(self.buttonlength/2)+(self.buttonlength/8))
    def press(self):
        if self.x<mouseX<self.x+self.buttonwidth and self.y<mouseY<self.y+self.buttonlength:
            return True
        else:
            return False


class NumberBubble(): #Creates all the number bubbles in chasing numbers game

    def __init__(self):
        self.gen_bubble()
        self.score = 0
        self.game = 0 #Keeps track if the game is still in progress (0=on and 1=off)
                
    def gen_bubble(self): # Generates all positions of the bubbles and numbers
        self.posX = [random.randint(25,670)]
        self.posY = [random.randint(75,400)]
        self.lowhigh = random.randint(1,2) # To determine if user should select the lowest or highest number (1 = Lowest, 2 = Highest)
        p = 1
        while p != 10: # Generate a list of 10 x and y pos.
            x = random.randint(25,670)
            y = random.randint(75,400)
            check = False
            for l in self.posX: #Checks to make sure bubbles don't overlap
                for j in self.posY:
                    if x in range(l-51,l+51) and y in range(j-37,j+37):
                        check = True
                        break
                if check == True:
                    break
            if check == False: # This is so it does not overlap
                self.posX.append(x)
                self.posY.append(y)
                p += 1

        self.number_list = [random.randint(1,99)]
        n = 1
        while n != 10: # Generate a list of 10 random int 
            num = random.randint(1,99)
            check = False
            for t in self.number_list: # Makes sure number does not already exist
                if num == t:
                    check = True

            if check == False:
                self.number_list.append(num)
                n += 1

      
    def display(self): # Creates the game screen
        self.game = 0
        if self.lowhigh == 1: # Displays lowest text
            displaytext("Extra Bold",255,35,"Select the LOWEST Number",350,50)
        if self.lowhigh == 2: # Displays Highest text
            displaytext("Extra Bold",255,35,"Select the HIGHEST Number",350,50)
        i = 0
        while i < len(self.posX): # Creates the bubbles
            fill(255)
            ellipse(self.posX[i],self.posY[i],50,36)
            displaytext("Bold",0,20,self.number_list[i],self.posX[i],self.posY[i]+8)
            i += 1

        scoretext = "Score: "+str(self.score) # Displays current score
        if len(number_scorelist) == 0:
            highscore = 0
        else:
            highscore = number_scorelist[0]
        highscoretext = "High Score: "+str(highscore)
        displaytext("Extra Bold",255,25,scoretext,100,450)
        displaytext("Extra Bold",255,25,highscoretext,100,485)
        
    def gameover(self): # This is for when the games over and resets variables
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
            
    def remove_bubble(self,index): # Removes bubbles when clicked
        self.posX.remove(self.posX[index])
        self.posY.remove(self.posY[index])
        self.number_list.remove(self.number_list[index])

            
    def press(self): # Function for when mouse is pressed
        OpenSansExtraBold = loadFont("OpenSans-Extrabold-48.vlw")
        if self.game == 0:
            i = 0
            if self.lowhigh == 1:
                numbertarget = min(self.number_list)
            if self.lowhigh == 2:
                numbertarget = max(self.number_list)
            while i < len(self.posX):
                if len(self.posX) == 1: # If bubble as last one on screen reenerates 10 new bubbles
                    fill(0,255,0)
                    textFont(OpenSansExtraBold,25)
                    textAlign(CENTER)
                    text("+1",100,425)
                    self.gen_bubble()
                    self.score += 1
                    break
                if mouseX in range(self.posX[i]-25,self.posX[i]+25): # Checks if mouse click within a bubble
                    if mouseY in range(self.posY[i]-18,self.posY[i]+18):
                        if numbertarget == self.number_list[i]: # Sees if correct bubble was correct
                            fill(0,255,0)
                            textFont(OpenSansExtraBold,25)
                            textAlign(CENTER)
                            text("+1",100,425)
                            self.remove_bubble(i)
                            self.score += 1
                            self.lowhigh = random.randint(1,2) # Randomizese to see if its low or high
                        elif self.score != 0: # minus a point from the score if pressed wrong one
                            fill(124,10,2)
                            textFont(OpenSansExtraBold,25)
                            textAlign(CENTER)
                            text("-1",100,425)
                            self.score -= 1    
                i += 1
        if self.game == 1: # Keeps track of presses on game overpage
            if exitgame.press() == True:
                global pagenumber
                pagenumber = 0
            if savescore.press() == True:
                global pagenumber
                pagenumber = 7
                global scoresub
                scoresub = 1 # Tells the scoreboard that it needs to be subimmited
                global gamename
                gamename = "Chase the Number" # Tells the score board which game to save it in
                
class Timer(): # Function that creates timer
    def __init__(self,sec):
        self.sec = sec
        self.starttimer = millis() # Looks at current time
        
    def update(self): # Updates the timer
        timetext = "Time Left: "+str(self.sec)
        displaytext("Extra Bold",255,35,timetext,550,475) 
        
        timedif = millis() - self.starttimer # Calculates difference between current time and start time
        
        if timedif >= 1000: # Checks to see if time difference is more then one second
            self.sec -= 1
            self.starttimer = millis() # Resets start time
    
        
    def timecheck(self): # Checks if there is time on the clock
        if self.sec >= 0:
            return True
        else:
            return False
# Creates button for each page
        
### HOME PAGE BUTTONS ###
chasing = Button(50,150,'Extra Large','Chase The Numbers')
number = Button(50,250,'Extra Large','Number Detective') 
game3 = Button(50,350,'Extra Large','Game 3')

### INSTRUCTION PAGE BUTTONS ###
gamestart = Button(25,425,'Large','Start Game')
viewboard = Button(425,425,'Large','View Scoreboard')
returnmenu = Button(288,425,'Small','Menu')
    
### NUMBER DETECTIVE BUTTONS ###
easybutton = Button(75,350,'Small','3 Digit')
medbutton = Button(275,350,'Small','4 Digit')
hardbutton = Button(475,350,'Small','5 Digit')
newmenu = Button(50,425,'Large','Menu')
newviewboard = Button(400,425,'Large','View Scoreboard')
submit_guess = Button(500,220,'Small','Submit')
    
### GAME OVER BUTTONS ###
exitgame = Button(25,425,'Large','Exit Game')
savescore = Button(425,425,'Large','Save Score')
    
### SCOREBOARD BUTTONS ###
submit = Button(550,250,'Small','Submit')

def startup(): # Create objects for class functions
    global gamebubble
    gamebubble = NumberBubble()
    global chasetimer
    chasetimer = Timer(60)
    
def displaytext(font,fontfill,fontsize,inputtext,posX,posY): # The function to create text
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
    startup()
    
    ### DOWNLOAD SCORES##
    with open ("numberscore.txt") as number_score: # Chasing Numbe Scores
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
    with open ("detectivescore1.txt") as detective1_score: # 3 degit scores
        i = 0
        global detective1_namelist
        detective1_namelist = []
        global detective1_scorelist
        detective1_scorelist = []
        lines = [x.replace('\n', '') for x in detective1_score.readlines()]
        while i != len(lines):
            detective1_namelist.append(lines[i])
            detective1_scorelist.append(int(lines[i+1]))
            i += 2
    with open ("detectivescore2.txt") as detective2_score: # 4 degit scores
        i = 0
        global detective2_namelist
        detective2_namelist = []
        global detective2_scorelist
        detective2_scorelist = []
        lines = [x.replace('\n', '') for x in detective2_score.readlines()]
        while i != len(lines):
            detective2_namelist.append(lines[i])
            detective2_scorelist.append(int(lines[i+1]))
            i += 2
    with open ("detectivescore3.txt") as detective3_score: # 5 digit scores
        i = 0
        global detective3_namelist
        detective3_namelist = []
        global detective3_scorelist
        detective3_scorelist = []
        lines = [x.replace('\n', '') for x in detective3_score.readlines()]
        while i != len(lines):
            detective3_namelist.append(lines[i])
            detective3_scorelist.append(int(lines[i+1]))
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
        
    if pagenumber == 1: # Set Up Chase the Numbers Page
        instructp("Chase The Numbers","INSTRUCTIONS:\n"
                  "- You will be asked to find the lowest or highest number in\na set of 10 numbers and destory it.\n"
                  "- You EARN 1 point for every number destroyed.\n"
                  "- Select the wrong number and LOSE 1 point.\n"
                  "- Clear the board as fast as possible to be presented with\n another set of 10 numbers.\n"
                  "- Beware! You only have 60 seconds to earn as many points \nas possible.\n")
    
    if pagenumber == 2: # Set Up Number Detevtive
        global difcheck
        if difcheck != 1:
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
            
        if difcheck == 1:
            displaytext("Extra Bold",255,30,"Select what scoreboard you want to view:",350,200)
            easybutton.create()
            medbutton.create()
            hardbutton.create()
        
    if pagenumber == 4: # Chase the Number Game Screen
        
        if chasetimer.timecheck() == True: # Checks to see if there is still time 
            gamebubble.display()
            chasetimer.update()
            
        else:
            global gamescore
            gamescore = gamebubble.gameover()
            
    if pagenumber == 5: #Number Detective Screen
        
        if digitguess == 0:
            if dif == 1:
                displaytext("Extra Bold",255,30,"Crack the code! You need to guess\nwhat the 3 digits of the code are...",350,50)
                leng = 3
            if dif == 2:
                displaytext("Extra Bold",255,30,"Crack the code! You need to guess\nwhat the 4 digits of the code are...",350,50)
                leng = 4
            if dif == 3:
                displaytext("Extra Bold",255,30,"Crack the code! You need to guess\nwhat the 5 digits of the code are...",350,50)
                leng = 5
            displaytext("Extra Bold",255,25,"Enter your guess:",175,255)
            guessbox.show()
            if len(guessbox.getText()) > leng: # Restricts entries to the digits needed
                inputtext = str(guessbox.getText())
                guessbox.setText(inputtext[:leng])
            submit_guess.create()
            scoretext = "Your Guesses: "+str(guesscounter)        
            displaytext("Extra Bold",255,25,scoretext,125,450)
            #displaytext("Extra Bold",255,25,highscoretext,100,485)
            displaytext("Extra Bold",255,25,digitinfo,525,375)
        
        if digitguess == 1: # Sees if the number is correctly gueesed
            displaytext("Extra Bold",255,50,"You Cracked the Code!",350,250)
            exitgame.create()
            savescore.create()
                
            
    if pagenumber == 7: #Scoreboard Screen
        
        if scoresub == 1:
            displaytext("Extra Bold",255,40,"Score Submission",350,50)
            if gamename == "Chase the Number":
                scoretxt = "Your Score: "+str(gamescore)
            if gamename == "Number Detective":
                scoretxt = "# of Guesses: "+str(gamescore)
            displaytext("Extra Bold",255,30,scoretxt,350,200)
            displaytext("Extra Bold",255,25,"Name:",100,290)
            global t
            if t == 0:
                font = createFont("OpenSansBold", 20)
                global cp5
                cp5 = ControlP5(this)
                global namebox
                namebox = cp5.addTextfield("Name Input").setLabel("").setPosition(175,250).setSize(
                350,60).setFont(font).setFocus(True).setColor(color(255)).setAutoClear(False)
                t = 1
            submit.create()
            
        if scoresub == 2:
            namebox.hide()
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
            if gamename == "Number Detective":
                i = 0
                while i < len(detective1_namelist) and i < 5 and dif == 1:
                        scoreboard_text += "\n"+detective1_namelist[i]+" - "+"Score: "+str(detective1_scorelist[i])+"\n"
                        i += 1
                while i < len(detective2_namelist) and i < 5 and dif == 2:
                        scoreboard_text += "\n"+detective2_namelist[i]+" - "+"Score: "+str(detective2_scorelist[i])+"\n"
                        i += 1
                while i < len(detective3_namelist) and i < 5 and dif == 3:
                        scoreboard_text += "\n"+detective3_namelist[i]+" - "+"Score: "+str(detective3_scorelist[i])+"\n"
                        i += 1
            displaytext("Regular",255,24,scoreboard_text,350,70)
            strokeWeight(1)
            returnmenu.create()
                

def mouseClicked():
    global gamename
    global pagenumber
    global scoresub
    global difcheck
    global dif
    global digit
    global digitguess
    global guessbox
    global cp5
    if pagenumber == 0: # Home Page Buttons
        if chasing.press() == True:
            pagenumber = 1
        if number.press() == True:
            pagenumber = 2
    if pagenumber == 1: # Chase the Numbers Instruction Buttons
        if gamestart.press() == True:
            pagenumber = 4
        if viewboard.press() == True:
            pagenumber = 7
            gamename = "Chase the Number"
            scoresub = 3
        if returnmenu.press() == True:
            pagenumber = 0
    if pagenumber == 2: # Number Detective Instruction Buttons
        if easybutton.press() == True:
            if difcheck != 1:
                pagenumber = 5
                dif = 1
                digit = random.randint(100,999)
                digitguess = 0
                font = createFont("OpenSansBold", 35)
                cp5 = ControlP5(this)
                guessbox = cp5.addTextfield("Guess Input").setLabel("").setPosition(325,200).setSize(
                120,100).setFont(font).setFocus(True).setColor(color(255)).setAutoClear(False).setInputFilter(ControlP5.INTEGER)
            if difcheck == 1:
                dif = 1
                pagenumber = 7
                difcheck = 0
        if medbutton.press() == True:
            if difcheck != 1:
                pagenumber = 5
                dif = 2
                digit = random.randint(1000,9999)
                digitguess = 0
                font = createFont("OpenSansBold", 35)
                cp5 = ControlP5(this)
                guessbox = cp5.addTextfield("Guess Input").setLabel("").setPosition(325,200).setSize(
                120,100).setFont(font).setFocus(True).setColor(color(255)).setAutoClear(False).setInputFilter(ControlP5.INTEGER)
            if difcheck == 1:
                dif = 2
                pagenumber = 7
                difcheck = 0
        if hardbutton.press() == True:
            if difcheck != 1:
                pagenumber = 5
                dif = 3
                digit = random.randint(10000,99999)
                digitguess = 0
                font = createFont("OpenSansBold", 35)
                cp5 = ControlP5(this)
                guessbox = cp5.addTextfield("Guess Input").setLabel("").setPosition(325,200).setSize(
                120,100).setFont(font).setFocus(True).setColor(color(255)).setAutoClear(False).setInputFilter(ControlP5.INTEGER)
            if difcheck == 1:
                dif = 3
                pagenumber = 7
                difcheck = 0
        if newviewboard.press() == True and difcheck != 1:
            difcheck = 1
            global gamename
            gamename = "Number Detective"
            global scoresub
            scoresub = 3
        if newmenu.press() == True and difcheck != 1:
            pagenumber = 0 
    
    if pagenumber == 4:
        gamebubble.press()
        
    if pagenumber == 5:
        if submit_guess.press() == True and digit == int(guessbox.getText()) and digitguess == 0:
            digitguess = 1
            global guesscounter
            guesscounter += 1
            guessbox.hide()
        elif submit_guess.press() == True and digit != int(guessbox.getText()) and len(str(digit)) == len(guessbox.getText()) and digitguess == 0:
            global guesscounter
            guesscounter += 1
            if digit < int(guessbox.getText()):
                loworhigh = "Too High"
            if digit > int(guessbox.getText()):
                loworhigh = "Too Low"
            digcorrect = 0
            if str(digit)[0:1] == str(guessbox.getText())[0:1]:
                digcorrect += 1
            if str(digit)[1:2] == str(guessbox.getText())[1:2]:
                digcorrect += 1
            if str(digit)[2:3] == str(guessbox.getText())[2:3]:
                digcorrect += 1
            if len(str(digit)) == 3:
                correcttext = str(digcorrect)+" out of 3 digits correct!"
            if len(str(digit)) == 4:
                if str(digit)[3:4] == str(guessbox.getText())[3:4]:
                    digcorrect += 1
                correcttext = str(digcorrect)+" out of 4 digits correct!"
            if len(str(digit)) == 5:
                if str(digit)[3:4] == str(guessbox.getText())[3:4]:
                    digcorrect += 1
                if str(digit)[4:5] == str(guessbox.getText())[4:5]:
                    digcorrect += 1
                correcttext = str(digcorrect)+" out of 5 digits correct!"
            global digitinfo
            digitinfo = "Guess: "+str(guessbox.getText())+"\nWrong!\n"+loworhigh+"\n"+correcttext
            guessbox.setText("")
            
        elif digitguess == 1:
            if exitgame.press() == True:
                global pagenumber
                pagenumber = 0
            if savescore.press() == True:
                global pagenumber
                pagenumber = 7
                global scoresub
                scoresub = 1
                global gamename
                gamename = "Number Detective"
                global gamescore
                gamescore = guesscounter
            
    if pagenumber == 7:
        if scoresub == 1 and submit.press() == True and namebox.getText() != "":
            global scoresub
            scoresub = 2
            global t
            t = 0
            if gamename == "Chase the Number":
                global number_namelist
                number_namelist.append(str(namebox.getText()))
                global number_scorelist
                number_scorelist.append(int(gamescore))
                sortedscore = sorted(number_scorelist, reverse= True)
                new_namelist = []
                for s in sortedscore:
                    indx = number_scorelist.index(s)
                    number_scorelist.pop(indx)
                    new_namelist.append(number_namelist[indx])
                    number_namelist.pop(indx)
                number_namelist = new_namelist
                number_scorelist = sortedscore
                with open ("numberscore.txt", "w") as number_score:
                    i = 0
                    while i < len(number_namelist):
                        number_score.write(str(number_namelist[i])+'\n')
                        number_score.write(str(number_scorelist[i])+'\n')
                        i += 1
            if gamename == "Number Detective" and dif == 1:
                global detective1_namelist
                detective1_namelist.append(str(namebox.getText()))
                global detective1_scorelist
                detective1_scorelist.append(int(gamescore))
                sortedscore = sorted(detective1_scorelist, reverse= False)
                new_namelist = []
                for s in sortedscore:
                    indx = detective1_scorelist.index(s)
                    detective1_scorelist.pop(indx)
                    new_namelist.append(detective1_namelist[indx])
                    detective1_namelist.pop(indx)
                detective1_namelist = new_namelist
                detective1_scorelist = sortedscore
                with open ("detectivescore1.txt", "w") as detective1_score:
                    i = 0
                    while i < len(detective1_namelist):
                        detective1_score.write(str(detective1_namelist[i])+'\n')
                        detective1_score.write(str(detective1_scorelist[i])+'\n')
                        i += 1
            if gamename == "Number Detective" and dif == 2:
                global detective2_namelist
                detective2_namelist.append(str(namebox.getText()))
                global detective2_scorelist
                detective2_scorelist.append(int(gamescore))
                sortedscore = sorted(detective2_scorelist, reverse= False)
                new_namelist = []
                for s in sortedscore:
                    indx = detective2_scorelist.index(s)
                    detective2_scorelist.pop(indx)
                    new_namelist.append(detective2_namelist[indx])
                    detective2_namelist.pop(indx)
                detective2_namelist = new_namelist
                detective2_scorelist = sortedscore
                with open ("detectivescore2.txt", "w") as detective2_score:
                    i = 0
                    while i < len(detective2_namelist):
                        detective2_score.write(str(detective2_namelist[i])+'\n')
                        detective2_score.write(str(detective2_scorelist[i])+'\n')
                        i += 1    
            if gamename == "Number Detective" and dif == 3:
                global detective3_namelist
                detective3_namelist.append(str(namebox.getText()))
                global detective3_scorelist
                detective3_scorelist.append(int(gamescore))
                sortedscore = sorted(detective3_scorelist, reverse= False)
                new_namelist = []
                for s in sortedscore:
                    indx = detective3_scorelist.index(s)
                    detective3_scorelist.pop(indx)
                    new_namelist.append(detective3_namelist[indx])
                    detective3_namelist.pop(indx)
                detective3_namelist = new_namelist
                detective3_scorelist = sortedscore
                with open ("detectivescore3.txt", "w") as detective3_score:
                    i = 0
                    while i < len(detective3_namelist):
                        detective3_score.write(str(detective3_namelist[i])+'\n')
                        detective3_score.write(str(detective3_scorelist[i])+'\n')
                        i += 1
        if scoresub != 1 and returnmenu.press() == True:
            pagenumber = 0
            
