from copy import deepcopy
import sys
class Game:
    
    def __init__(self,state,curP,maxP,playercount):
        self.state = state
        self.curP= curP
        self.maxP= maxP
        self.playercount = playercount
    def __str__(self):
        output = "_____________________________\n"
        
        for col in range(6):
            output+="| "
            for row in range(7):
                output+=str(self.state[col][row])+" | "
            output+="\n"
            output+= "_____________________________\n"
            
        return output
        
    def play(self,col):
        if col>6 or col <0:
            return False
        if self.playercount[col]==6:
            return False
        row = self.playercount[col]+1
        self.state[6-row][col]=self.curP
        self.curP = int(1) if self.curP is int(2) else int(2)
        self.playercount[col]+=1
        return True
     
    def quadrupleCheck (self, pattern1, pattern2):
        num1 = 0
        num2 = 0
        for row in self.state:
            temp = row[0:4]
            temp.sort()
            if  temp == pattern1:
                num1 += 1
            temp = row[1:5]
            temp.sort()
            if temp == pattern1:
                num1 += 1
            temp = row[2:6]
            temp.sort()
            if temp == pattern1:
                num1 += 1
            temp = row[3:7]
            temp.sort()
            if temp == pattern1:
                num1 += 1
            #For Player 2
            temp = row[0:4]
            temp.sort()
            if  temp == pattern2:
                num2 += 1
            temp = row[1:5]
            temp.sort()
            if temp == pattern2:
                num2 += 1
            temp = row[2:6]
            temp.sort()
            if temp == pattern2:
                num2 += 1
            temp = row[3:7]
            temp.sort()
            if temp == pattern2:
                num2 += 1
        for j in range(7):
            temp = [self.state[0][j], self.state[1][j], self.state[2][j], self.state[3][j]]
            temp.sort()
            if temp == pattern1:
                num1 += 1
            if temp == pattern2:
                num2 += 1
            temp = [self.state[1][j], self.state[2][j], self.state[3][j], self.state[4][j]]
            temp.sort()
            if temp == pattern1:
                num1 += 1
            if temp == pattern2:
                num2 += 1
            temp = [self.state[2][j], self.state[3][j], self.state[4][j], self.state[5][j]]
            temp.sort()
            if temp == pattern1:
                num1 += 1
            if temp == pattern2:
                num2 += 1
        temp = [self.state[0][0], self.state[1][1], self.state[2][2], self.state[3][3]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][0], self.state[2][1], self.state[3][2], self.state[4][3]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][0], self.state[3][1], self.state[4][2], self.state[5][3]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[0][1], self.state[1][2], self.state[2][3], self.state[3][4]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][1], self.state[2][2], self.state[3][3], self.state[4][4]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][1], self.state[3][2], self.state[4][3], self.state[5][4]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[0][2], self.state[1][3], self.state[2][4], self.state[3][5]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][2], self.state[2][3], self.state[3][4], self.state[4][5]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][2], self.state[3][3], self.state[4][4], self.state[5][5]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[0][3], self.state[1][4], self.state[2][5], self.state[3][6]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][3], self.state[2][4], self.state[3][5], self.state[4][6]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][3], self.state[3][4], self.state[4][5], self.state[5][6]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[0][6], self.state[1][5], self.state[2][4], self.state[3][3]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][6], self.state[2][5], self.state[3][4], self.state[4][3]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][6], self.state[3][5], self.state[4][4], self.state[5][3]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[0][5], self.state[1][4], self.state[2][3], self.state[3][2]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][5], self.state[2][4], self.state[3][3], self.state[4][2]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][5], self.state[3][4], self.state[4][3], self.state[5][2]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[0][4], self.state[1][3], self.state[2][2], self.state[3][1]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][4], self.state[2][3], self.state[3][2], self.state[4][1]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][4], self.state[3][3], self.state[4][2], self.state[5][1]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[0][3], self.state[1][2], self.state[2][1], self.state[3][0]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[1][3], self.state[2][2], self.state[3][1], self.state[4][0]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        temp = [self.state[2][3], self.state[3][2], self.state[4][1], self.state[5][0]]
        temp.sort()
        if temp == pattern1:
            num1 += 1
        if temp == pattern2:
            num2 += 1
        return [num1, num2]
	
    
    def evaluateFunction(self):
        weight1 = 0.001
        weight2 = 0.01
        weight3 = 0.1
        weight4 = 1
        [score1_4Row,score2_4Row] = self.quadrupleCheck([1,1,1,1],[2,2,2,2])
        [score1_3Row,score2_3Row] = self.quadrupleCheck([0,1,1,1],[0,2,2,2])   
        [score1_2Row,score2_2Row] = self.quadrupleCheck([0,0,1,1],[0,0,2,2])
        [score1_1Row,score2_1Row] = self.quadrupleCheck([0,0,0,1],[0,0,0,2])
        score1 = score1_4Row *weight4 + weight3 * score1_3Row + weight2 * score1_2Row + weight1 * score1_1Row
        score2 = score2_4Row *weight4+ weight3 * score2_3Row + weight2 * score2_2Row + weight1 * score2_1Row
        if self.maxP == 1:
            return score1-score2
        else:
            return score2-score1

def maxVal(game,alpha,beta,d):
    if (sum(game.playercount) == 42) or (d == depthLimit):
        value = game.evaluateFunction()
        return value
    value = float('-Inf')
    for i in range(7):
        nextState = deepcopy(game)
        if nextState.play(i):
            tvalue = minVal(nextState,alpha,beta,d+1)
            if tvalue >value:
                value = tvalue                
                if value >= beta:
                    return value
                if alpha > value:
                    alpha = value
    return value

def minVal(game,alpha,beta,d): 
    if (sum(game.playercount) == 42) or (d == depthLimit):
        value = game.evaluateFunction()
        return value
    value = float('Inf')
    for i in range(7):
        nextState = deepcopy(game)
        if nextState.play(i):
            tvalue = maxVal(nextState,alpha,beta,d+1)
            if tvalue <value:
                value = tvalue
                if value <= alpha:
                    return value
                if value < beta:
                    beta = value
    return value
        
    
    
def minmax(game):
    if sum(game.playercount) == 42:
        return [None,-1]
    alpha = float('-Inf')
    beta = float('Inf')
    optimalMove = -1
    value =float("-Inf")
    for i in range(7):
        nextState = deepcopy(game)
        if nextState.play(i):
            tvalue = minVal(nextState,alpha,beta,1)
            if tvalue >value:
                value = tvalue
                optimalMove = i
                if value > alpha:
                    alpha = value
    return [optimalMove,value] 
        
def readFile(fileName): #Read game from file.
    try:
        f1 = open(fileName,'r')
    except :
        sys.exit("Unable to Open File")
    lines = f1.readlines()
    game = [[int(char) for char in line[0:7]] for line in lines[0:-1]]
    player = int(lines[-1][0])
    f1.close()
    playercount=[]
    for row in range(7):   
        temp=[]
        for col in range(6):
            if game[col][row]>0:
                temp.append(1)
        playercount.append(sum(temp))
        
    return [game, player,playercount]

def writeFile(fileName, game): 
	try:
		f1 = open(fileName,'w')
	except IOError:
		sys.exit("Cannot open Output File. Please Check Again")
	for row in game.state:
		f1.write(''.join(str(col) for col in row) + '\r\n')
	f1.write('%s\r\n' % str(game.curP))
	f1.close()
	
def humanMove(game):
    try:
        col = input("Please enter Column No. from 1 to 7: ")
    except EOFError:
        sys.exit("Terminated at Keyboard")
    col = int(col) - 1
    if  col < 0:
        print ("Invalid Move.Column no. cannot be <0.Enter valid number.Please Try again.")
        return humanMove(game)
    if  col > 6:
        print ("Invalid Move.Column no. exceeding the limit. Please Try again.")
        return humanMove(game)
    if game.playercount[col] == 6:
        print ("Invalid Move. Piece cannot be placed in that position. Please Try again.")
        return humanMove(game)
    game.play(col)
    return game
	
depthLimit = 20
def main():
    if len(sys.argv) != 5:
        sys.exit("Incorrect number of arguments: Try again...\ncommand line argument need to be in below mentioned Format:\n \tInteractive Mode: connect.py interactive [input_file] [computer-next/human-next] [depth]\n\tOne-Move mode: maxconnect4.py one-move [input_file] [output_file] [depth]")    
    if sys.argv[1] == 'interactive' or sys.argv[1] == 'one-move':
        mode = sys.argv[1]
    else:
        sys.exit("Unknown Mode.\n")
    [state,player,playercount] = readFile(sys.argv[2])
    global depthLimit 
    depthLimit= int(sys.argv[4])
    if mode == "one-move":
        game = Game(state,player,player,playercount)
        [action, pay] = minmax(game)
        if action is not None:
            if game.play(action):
                writeFile(sys.argv[3],game)
        else:
            print ("Game cannot be played.Game board is full.")
    else:
        if sys.argv[3] == 'human-next':
            compTurn = False
            humanPlayer = player
            if player == 1:
                game = Game(state,player,2,playercount)
            else:
                game = Game(state,player,1,playercount)
        elif sys.argv[3] == 'computer-next':
            compTurn = True
            game = Game(state,player,player,playercount)
            if player == 1:
                humanPlayer = 2
            else:
                humanPlayer = 1
        else:
            sys.exit("Options for interactive mode are computer-next/human-next")
        print(str(game))
        while sum(game.playercount) < 42:
            if compTurn:
                print ('Computing in Progress')
                [act, payoff] = minmax(game)
                if act is not None:
                    game.play(act)
                    print("Score: ")
                    [points1,points2]= game.quadrupleCheck([1,1,1,1],[2,2,2,2])
                    print(" Player1 - "+str(points1)+"\n Player2 - "+str(points2))
                    
                    writeFile('computer.txt',game)
                compTurn = False
            else:
                print("Your Turn (You Play "+str(humanPlayer)+" )")
                game = humanMove(game)
                writeFile('human.txt',game)
                compTurn = True
            print(str(game))
        print("Game Over")
        print(" Player1 - "+str(points1)+"\n Player2 - "+str(points2))
        

main()