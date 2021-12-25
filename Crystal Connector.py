#Crystal Connector
#Crsytalconnector.py
#Daniel Rose
#drose04
##section 2

#This is a game about connecting crystals



#Import functions
from graphics import*
import random
import time
import copy

            
#Stores each crystal, what type they are and if they need to be cleated or not CLOD
class Crystal:
    #initilization
    def __init__(self, type):
        self.type = type
        self.broken = False
        self.cystal = Image(Point(0,0), "c1.ppm")
        
    #give you crystal type
    def getType(self):
        return self.type
    
    #set the crystal type
    def setType(self, type):
        self.type = type
    
    #Tells you if the crsytal should be broken
    def getBroken(self):
        return self.broken
    
    #Will set the crstal to be broken
    def setBroken(self, broken):
        self.broken = broken
        
    #draw each crystal
    def img(self, win, x, y):
        if self.type == 1:
            self.crystal = Image(Point(x,y), "c1.ppm")
            self.crystal.draw(win)
        if self.type == 2:
            self.crystal = Image(Point(x,y), "c2.ppm")
            self.crystal.draw(win)
        if self.type == 3:
            self.crystal = Image(Point(x,y), "c3.ppm")
            self.crystal.draw(win)
        if self.type == 4:
            self.crystal = Image(Point(x,y), "c4.ppm")
            self.crystal.draw(win)
        if self.type == 5:
            self.crystal = Image(Point(x,y), "c5.ppm")
            self.crystal.draw(win)
        if self.type == 6:
            self.crystal = Image(Point(x,y), "c6.ppm")
            self.crystal.draw(win)
            
    #undraw each crystal        
    def remove(self):
        self.crystal.undraw()
        
#Welsome screen for the program
def welcomeScreen(win):
    #Draw all the text OTXT
    welcome = Text(Point(20,65), "Welcome to Crystal Connector!")
    welcome.setSize(35)
    welcome.draw(win)
    name = Entry(Point(20,42.5), 20)
    nametext = Text(Point(20,50),"Enter your name here")
    nametext.setSize(20)
    nametext.draw(win)
    name.draw(win)
    continuebox = Rectangle(Point(0,30),Point(40,35))
    text = Text(Point(20,32.5), "Continue")
    continuebox.draw(win)
    text.draw(win)
    #detect for mouse click
    t = 1
    while t == 1:
        x,y = mouseCords(win)
        if 0 < x < 40:
            if 30 < y < 35:
                #IEB detect that you entered actual text in the text box or if it too long
                if name.getText() == '' or len(name.getText()) > 15:
                    error = Text(Point(20,20), "Please type a name no longer then 15 characters")
                    error.setSize(15)
                    error.draw(win)
                else:
                    t = 0
                
    username = name.getText()
    #Close Everything
    welcome.undraw()
    nametext.undraw()
    name.undraw()
    text.undraw()
    continuebox.undraw()
    return username


#draws the grid and the side text
def gameScreenGrid(win):
    #draws the text on the side
    scoretext = Text(Point(-20,70), "Score")
    scoretext.setSize(20)
    scoretext.draw(win)
    turntext = Text(Point(-20,40), "Turns Left")
    turntext.setSize(20)
    turntext.draw(win)
    #draws vertical and horizontal lines for the grid
    for i in range(0 ,81, 10):
        line = Line(Point(i,0),Point(i,80))
        line.draw(win)
    for i in range(0 ,81, 10):
        line = Line(Point(0,i),Point(80,i))
        line.draw(win)
    
    
#create a random crystal CLOD
def randomCrystal():
    type = random.randrange(1,7)
    crystal = Crystal(type)
    return crystal
    
    
#function  returns x and why cordinate to get easily IMS          
def mouseCords(win):
    point = win.getMouse()
    x = point.getX()
    y = point.getY()
    return x,y
    

#creates a random board of crystals RND LOOD
def randomBoard(win):
    r0=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    r1=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    r2=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    r3=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    r4=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    r5=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    r6=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    r7=[randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal(),randomCrystal()]
    board = [r0,r1,r2,r3,r4,r5,r6,r7]
    
    return board

#draws every crystal in its correct position
def drawBoard(win, board):
    for y in range (0, 8):
        for x in range(0,8):
            board[y][x].img(win, x*10+5, y*10+5)
            
#will erase the whole board          
def eraseBoard(win, board):
    for y in range (0, 8):
        for x in range(0,8):
            if board[y][x].getBroken() == False:
                board[y][x].remove()

#makes every crystals broken value to false
def falseBoard(board):
    for y in range (0, 8):
        for x in range(0,8):
            board[y][x].setBroken(False)
    return board

#this checks for pairs on the board and will caclculate what to add to the score
#it will also set 
def checkBoard(board, win, scoreadd):
    scoreadd = scoreadd
    extraturn = 0
    match = False
    #Check for matches horizontally
    for y in range(0,8):
        for x in range(0,6):
            #check for 3 in a row
            if board[y][x].getType() == board[y][x+1].getType():
                if board[y][x].getType() == board[y][x+2].getType():
                    board[y][x].setBroken(True)
                    board[y][x+1].setBroken(True)
                    board[y][x+2].setBroken(True)
                    match = True
                    scoreadd = scoreadd + 30
                    #check for 4 in a row
                    if x < 5:
                        if board[y][x].getType() == board[y][x+3].getType():
                            extraturn = extraturn + 1
                            scoreadd = scoreadd + 10
    #Check for matches vertically
    for y in range(0,6):
        for x in range(0,8):
            #check for 3 in a row
            if board[y][x].getType() == board[y+1][x].getType():
                if board[y][x].getType() == board[y+2][x].getType():
                    board[y][x].setBroken(True)
                    board[y+1][x].setBroken(True)
                    board[y+2][x].setBroken(True) 
                    match = True
                    scoreadd = scoreadd + 30
                    #check for 4 in a row
                    if y < 5:
                        if board[y][x].getType() == board[y+3][x].getType():
                            extraturn = extraturn + 1
                            scoreadd = scoreadd + 10
                    
    return board, match, extraturn, scoreadd
    
#This will clear all the broken crystals from the screen
def clearBroken(board, win, scoreadd):
    scoreadd = scoreadd
    e = True #false
    for y in range(0,8):
        for x in range(0,8):
            broken = board[y][x].getBroken()
            if broken == True:
                board[y][x].remove()
                e = True
    #if there is another match it will call downboard again to continue to clear the new matches
    if e == True:
        board, scoreadd = downBoard(board,win, scoreadd)
    return board, scoreadd
        
#this will move all the crystals above the broken crystals down to fill the board
def downBoard(board,win, scoreadd):
    scoreadd = scoreadd
    for x in range(0,8):
        for y in range(0,8):
            if board[y][x].getBroken() == True:
                h = y+1
                while h <=7:
                    if board[h][x].getBroken() == False:
                        board[y][x].setType(board[h][x].getType())
                        board[h][x].setBroken(True)
                        break
                    elif h == 7:
                        board[y][x].setType(random.randrange(1,7))
                    h = h+1
        if board[7][x].getBroken() == True:
            board[7][x].setType(random.randrange(1,7))
    #draw the new board when it is done moveing them down
    drawBoard(win, board)
    #puts the board back to unbroken
    board = falseBoard(board)
    board, match, extraturn, scoreadd = checkBoard(board, win, scoreadd)
    #runs again if there is another pair of on the board
    if match == True:
        time.sleep(1.25)
        board, scoreadd = clearBroken(board, win, scoreadd)
    
    return board, scoreadd
    
#give the x and y cords of your mouse click and divides by 10 to give the box number
def detectClick(board,win):
    x,y = mouseCords(win)
    while x < 0:
        x,y = mouseCords(win)
    x = int(x//10)
    y = int(y//10)
    return(x,y)

#draws invalid move to the screen
def invalidMove(win):
    error=Text(Point(-20,15), 'Invalid Move')
    error.setSize(20)
    error.draw(win)
    time.sleep(2)
    error.undraw()
    
#Displays the endscreen text and Latest Scores    
def endScreen(win, score, username):
    blankscreen = Rectangle(Point(-40,-1), Point(81,81))
    blankscreen.setFill('white')
    blankscreen.draw(win)
    
    endgame = Text(Point(20,75), 'Game Over')
    endgame.setSize(30)
    endgame.draw(win)
    scoretext = Text(Point(20,65), 'Your Score: ' + str(score))
    scoretext.setSize(20)
    scoretext.draw(win)
    
    #Adds your score to the file OFL
    leardboardfile = open('leaderboard.txt', 'a')
    leardboardfile.write('\n' + str(username) + '\t' + str(score))
    leardboardfile.close()
    
    #reads the names and scores of previous games from a file IFL
    leaderboardfile = open('leaderboard.txt', 'r')
    leaderboard = leaderboardfile.readlines()
    leaderboardfile.close()
    llen = len(leaderboard)
    names = ['']*llen
    scores = ['']*llen
    i = 0
    while i < llen:
        tempinfo = leaderboard[i].split('\t')
        names[i] = tempinfo[0]
        if i == llen-1:
            scores[i] = int(tempinfo[1])
        else:
            scores[i] = int(tempinfo[1][:-1])
        i = i + 1
        
    #Draw the scores to the screen
    scoretext = Text(Point(20,57.5), 'Latest Scores')
    scoretext.setSize(20)
    scoretext.draw(win)
    line = Line(Point(-10,53.75),Point(50,53.75))
    line.setWidth(2)
    line.draw(win)
    line = Line(Point(-10,25),Point(50,25))
    line.setWidth(2)
    line.draw(win)
    i = llen-1
    down = 0
    while i > llen-6:
        playername = Text(Point(10, 50-down*5), names[i])
        playerscore = Text(Point(30, 50-down*5), scores[i])
        playername.setSize(20)
        playerscore.setSize(20)
        playername.draw(win)
        playerscore.draw(win)
        i = i - 1
        down = down + 1
        
    click = Text(Point(20,20), 'Click to close the game')
    click.setSize(20)
    click.draw(win)
    win.getMouse()
#This runs the gameplay section
def mainGame(board, win):
    score = 0
    turns = 10
    scoreisplay=Text(Point(-20,65), score)
    scoreisplay.setSize(20)
    scoreisplay.draw(win)
    turndisplay=Text(Point(-20,35), turns)
    turndisplay.setSize(20)
    turndisplay.draw(win)
    #The game is played in this loop for the ammount of turns
    while turns > 0:
        #detect the first box clicked
        x1,y1 = detectClick(board,win)
        box = Rectangle(Point(x1*10,y1*10),Point((x1*10)+10,(y1*10)+10))
        box.setOutline('red')
        box.setWidth(5)
        box.draw(win)
        
        #dectect the second box clicked
        x2,y2 = detectClick(board,win)
        box2 = Rectangle(Point(x2*10,y2*10),Point((x2*10)+10,(y2*10)+10))
        box2.setOutline('red')
        box2.setWidth(5)
        box2.draw(win)
        time.sleep(.25)
        box.undraw()
        box2.undraw()
        scoreadd = 0
        #makes sure the boxes are adjecent
        if -2 < (x1-x2) < 2:
            if -2 < (y1-y2) < 2:
                #swap the crystals
                temp = board[y1][x1].getType()
                board[y1][x1].setType(board[y2][x2].getType())
                board[y2][x2].setType(temp)
                drawBoard(win, board)
                time.sleep(.25)
        
                #check for a match if there is a match modify the board
                board, match, extraturn, scoreadd = checkBoard(board, win, scoreadd)
                if match == False:
                    temp = board[y1][x1].getType()
                    board[y1][x1].setType(board[y2][x2].getType())
                    board[y2][x2].setType(temp)
                    drawBoard(win, board)
                    invalidMove(win)
                elif match == True:
                    #clear the board untill nothing no matches are left
                    board, scoreadd = clearBroken(board, win,scoreadd)
                    turns = turns + extraturn
                    turns = turns - 1
                    turndisplay.undraw()
                    turndisplay=Text(Point(-20,35), turns)
                    turndisplay.setSize(20)
                    turndisplay.draw(win)
                    score = score + scoreadd
                    scoreisplay.undraw()
                    scoreisplay=Text(Point(-20,65), score)
                    scoreisplay.setSize(20)
                    scoreisplay.draw(win)
            else:
                #the crystals selected are not right next to eachocher
                invalidMove(win)
        else:
            #the crystals selected are not right next to eachocher
            invalidMove(win)
            
    #get the game scpre
    return score
#main
    
def main():
    #Create Window GW
    win = GraphWin("Crystal Connector", 900, 600)
    win.setBackground("white")
    win.setCoords(-40,-1,81,81)
    #Welcom screen where it will get your name FNC
    username = welcomeScreen(win)
    #Show the rules untill you click the button
    rules = Image(Point(20,40), "rules.gif")
    rules.draw(win)
    click = win.getMouse()
    #draw a white rectangle to cleat the
    blankscreen = Rectangle(Point(-40,-1), Point(81,81))
    blankscreen.setFill('white')
    blankscreen.draw(win)
    #Draw the grid
    scoreadd = 0
    #Draw the game sidetext and grid
    gameScreenGrid(win)
    #create a random board of crystals
    board = randomBoard(win)
    #draw the crystals
    drawBoard(win, board)
    #check the board for matches
    checkBoard(board, win,scoreadd)
    #clear the board of matches
    board, scoreadd = clearBroken(board, win,scoreadd)
    #run the game portion
    score = mainGame(board,win)
    time.sleep(1)
    #show the endscreen
    endScreen(win, score, username)
    win.close()
main()