# Naughts-and-crosses
import random       #Means we can make the computer works
from termcolor import colored, cprint        #Means we can have coloured text!

def three_In_Row():     
    
    """Nat Lowis
    Checks if we have a three in a row anywhere"""
    
    for row in range(0,len(myArray)):                   #Checks if we have a three in a row along a row.  If we do we return which side has a three in a row
        if myArray[row] == ["x", "x", "x"]:
            return "X"
        elif myArray[row] == ["o", "o", "o"]:
            return "O"
            

    for col2 in range(0, len(myArray)):         #Checks if we have a column by making a new list which contains the three posistions we have
        newList =[]
        for row2 in range(0, len(myArray)):
            newList.append(myArray[row2][col2])
           
        if newList == ["x", "x", "x"]:
            return "X"
        elif newList == ["o", "o", "o"]:
            return "O"
    
    #Checks along the diagonal lines checking if we have a three in a diagonal
    if myArray[0][0] == "x" and myArray[1][1] == "x" and myArray[2][2] == "x":
        return "X"
    elif myArray[0][0] == "o" and myArray[1][1] == "o" and myArray[2][2] == "o":
        return "O"
    elif myArray[0][2] == "x" and myArray[1][1] == "x" and myArray[2][0] == "x":
        return "X"
    elif myArray[0][2] == "o" and myArray[1][1] == "o" and myArray[2][0] == "o":
        return "O"
            
def any_Spaces():
    
    """Nat Lowis
    Checks if we have any spaces left"""
    
    total = 0       #sets total of paces to 0
    for row in range(0, len(myArray)):
        for col in range(0, len(myArray[0])):
            if myArray[row][col] == " ":        # If thereis a space total increments by 1
                total = total + 1
        
    return total
    
def your_Turn():
    """Nat Lowis
    Asks user to enter where they want to enter their posistion"""
    again = True            #this makes sure you can enter an x to a posistion which has a space in it
    while again == True:
    
        rowStr = input("\nPlease enter your row number: ")            #Enter a row number

        while rowStr not in ["3", "1", "2"]:     #If not in this list user asked to enter again
            rowStr = input("Please enter a number between 1 and 3 inclusive: ")
            
        colStr = input("\nPlease enter your column number: ")     #User enter a column number

        
        while colStr not in ["3", "1", "2"]:            #If not in this list user has to enter again
            colStr = input("Please enter a number between 1 and 3 inclusive: ")
        
        rowNumber = int(rowStr)            #Changed to an integer so you can enter it to an array
        colNumber = int(colStr)
        
        colInt = colNumber - 1
        rowInt = rowNumber - 1
    
        if myArray[rowInt][colInt] == " ":      #If there is a space in the array it enters an x
            myArray[rowInt][colInt] = "x"
            again = False
        else:
            print("This space is already got an x or an o in it")
            
def your_Turn2():
    """Nat Lowis
    Asks user to enter where they want to enter their posistion"""
    again = True            #this makes sure you can enter an x to a posistion which has a space in it
    while again == True:
    
        rowStr = input("\nPlease enter your row number: ")            #Enter a row number

        while rowStr not in ["3", "1", "2"]:     #If not in this list user asked to enter again
            rowStr = input("Please enter a number between 1 and 3 inclusive: ")
            
        colStr = input("\nPlease enter your column number: ")     #User enter a column number
        
        while colStr not in ["3", "1", "2"]:            #If not in this list user has to enter again
            colStr = input("Please enter a number between 1 and 3 inclusive: ")
        
        rowNumber = int(rowStr)            #Changed to an integer so you can enter it to an array
        colNumber = int(colStr)
        
        colInt = colNumber - 1
        rowInt = rowNumber - 1
    
        if myArray[rowInt][colInt] == " ":      #If there is a space in the array it enters an x
            myArray[rowInt][colInt] = "o"
            again = False
        else:
            print("This space is already got an x or an o in it")
            
def computer_turn():
    """Nat Lowis
    Random posistion placing"""
    
    again2 = True
    tries = 0
    while again2 == True:
        row = random.randint(0,2)   #Selects a random number between 0 and 2
        column = random.randint(0,2) # Selects a random numnber between 0 and 2
        tries = tries + 1
        if myArray[row][column] == " ":
            myArray[row][column] = "o"  #Adds an o where row and column is
            again2 = False       
            
        elif tries == 9:        #If tries is equal to 9 I have decided there will be a full board
            again2 = False
            
def computer_turn2():
    """Nat Lowis
    Random posistion placing"""
    
    again2 = True
    tries = 0
    while again2 == True:
        row = random.randint(0,2)   #Selects a random number between 0 and 2
        column = random.randint(0,2) # Selects a random numnber between 0 and 2
        tries = tries + 1
        if myArray[row][column] == " ":
            myArray[row][column] = "x"  #Adds an o where row and column is
            again2 = False       
            
        elif tries == 50:        #If tries is equal to 50 I have decided there will be a full board
            again2 = False
        
def output_board():
    
    """Nat Lowis 
    Outputs he board"""
    print("    Column")
    print("    1,2,3")        #Prints the column numbers
    
    secondTotal = 0
    for row in range(0, len(myArray)):          #This will output the board 
        total = 1   #total  = 1
        
        for col in range(0, len(myArray[0])):           
            if total == 3:          #If total is 3 it means it is the third column
                print(myArray[row][col])
            elif total == 1:        #If it is the first column it will output the row number and the posistion
                strRow = str(row + 1)
                if secondTotal == 0:
                    print("R", strRow + "|", myArray[row][col], end = ",")
                    secondTotal = secondTotal + 1
                elif secondTotal == 1:
                    print("o", strRow + "|", myArray[row][col], end = ",")
                    secondTotal = secondTotal + 1
                elif secondTotal == 2:
                    print("w", strRow + "|", myArray[row][col],  end = ",")
                    secondTotal = secondTotal + 1
            else:
                print(myArray[row][col], end = ",")
            total = total + 1
        
def computer_turn_strageical(difficultyToUse):
    
    """Computer tries to stop you or win the game"""
    
    if difficultyToUse != "2":
    
        for row3 in range(0,len(myArray)):          #Will place a o in a posistion to win
    
            if myArray[row3] == ["o", "o", " "]:
                return row3, 2
            
            elif myArray[row3] == ["o", " ", "o"]:
                return row3, 1
        
            elif myArray[row3] == [" ", "o", "o"]:
                return row3, 0
            
            for col2 in range(0, len(myArray)): #Will place a o in a posistion to win 
                newList =[]
                for row2 in range(0, len(myArray)):
                    newList.append(myArray[row2][col2])
           
                if newList == ["o", "o", " "]:              
                    return 2,col2
            
                elif newList == [" ", "o", "o"]:
                    return 0, col2
            
                elif newList == ["o", " ", "o"]:
                    return 1, col2
            
    #Will place a o in a posistion to win        
        if myArray[0][0] == "o" and myArray[1][1] == "o" and myArray[2][2] == " ":
            return 2,2
        
        elif myArray[0][0] == "o" and myArray[1][1] == " " and myArray[2][2] == "o":
            return 1,1
        
        elif myArray[0][0] == " " and myArray[1][1] == "o" and myArray[2][2] == "o":
            return 0,0
        
        elif myArray[0][2] == " " and myArray[1][1] == "o" and myArray[2][0] == "o":
            return 0,2
        
        elif myArray[0][2] == "o" and myArray[1][1] == " " and myArray[2][0] == "o":
            return 1,1
        
        elif myArray[0][2] == "o" and myArray[1][1] == "o" and myArray[2][0] == " ":
            return 2,0
    
        for row in range(0,len(myArray)):
            if myArray[row] == ["x", "x", " "]:
                return row, 2
            
            elif myArray[row] == ["x", " ", "x"]:
                return row, 1
        
            elif myArray[row] == [" ", "x", "x"]:
                return row, 0
            
        #Stops x winning
        for col2 in range(0, len(myArray)):
            newList =[]
            for row2 in range(0, len(myArray)):
                newList.append(myArray[row2][col2])
           
            if newList == ["x", "x", " "]:              
                return 2,col2
            
            elif newList == [" ", "x", "x"]:
                return 0, col2
            
            elif newList == ["x", " ", "x"]:
                return 1, col2
        #Stops x winning        
        if myArray[0][0] == "x" and myArray[1][1] == "x" and myArray[2][2] == " ":
            return 2,2
        
        elif myArray[0][0] == "x" and myArray[1][1] == " " and myArray[2][2] == "x":
            return 1,1
        
        elif myArray[0][0] == " " and myArray[1][1] == "x" and myArray[2][2] == "x":
            return 0,0
        
        elif myArray[0][2] == " " and myArray[1][1] == "x" and myArray[2][0] == "x":
            return 0,2
        
        elif myArray[0][2] == "x" and myArray[1][1] == " " and myArray[2][0] == "x":
            return 1,1
        
        elif myArray[0][2] == "x" and myArray[1][1] == "x" and myArray[2][0] == " ":
            return 2,0
            
    else:
        
        for row3 in range(0,len(myArray)):          #Will place a o in a posistion to win
    
            if myArray[row3] == ["o", "o", " "]:
                return row3, 2
            
            elif myArray[row3] == ["o", " ", "o"]:
                return row3, 1
        
            elif myArray[row3] == [" ", "o", "o"]:
                return row3, 0
            
            for col2 in range(0, len(myArray)): #Will place a o in a posistion to win 
                newList =[]
                for row2 in range(0, len(myArray)):
                    newList.append(myArray[row2][col2])
           
                if newList == ["o", "o", " "]:              
                    return 2,col2
            
                elif newList == [" ", "o", "o"]:
                    return 0, col2
            
                elif newList == ["o", " ", "o"]:
                    return 1, col2
            
    #Will place a o in a posistion to win        
        if myArray[0][0] == "o" and myArray[1][1] == "o" and myArray[2][2] == " ":
            return 2,2
        
        elif myArray[0][0] == "o" and myArray[1][1] == " " and myArray[2][2] == "o":
            return 1,1
        
        elif myArray[0][0] == " " and myArray[1][1] == "o" and myArray[2][2] == "o":
            return 0,0
        
        elif myArray[0][2] == " " and myArray[1][1] == "o" and myArray[2][0] == "o":
            return 0,2
        
        elif myArray[0][2] == "o" and myArray[1][1] == " " and myArray[2][0] == "o":
            return 1,1
        
        elif myArray[0][2] == "o" and myArray[1][1] == "o" and myArray[2][0] == " ":
            return 2,0
            
def computer_turn_strageical2(difficultyToUse):
    
    """Computer tries to stop you or win the game"""
    
    if difficultyToUse != "2":
    
        for row3 in range(0,len(myArray)):          #Will place a o in a posistion to win
        
            if myArray[row3] == ["x", "x", " "]:
                return row3, 2
            
            elif myArray[row3] == ["x", " ", "x"]:
                return row3, 1
        
            elif myArray[row3] == [" ", "x", "x"]:
                return row3, 0
            
            for col2 in range(0, len(myArray)): #Will place a o in a posistion to win 
                newList =[]
                for row2 in range(0, len(myArray)):
                    newList.append(myArray[row2][col2])
           
                if newList == ["x", "x", " "]:              
                    return 2,col2
            
                elif newList == [" ", "x", "x"]:
                    return 0, col2
                
                elif newList == ["x", " ", "x"]:
                    return 1, col2
            
        #Will place a o in a posistion to win        
        if myArray[0][0] == "x" and myArray[1][1] == "x" and myArray[2][2] == " ":
            return 2,2
        
        elif myArray[0][0] == "x" and myArray[1][1] == " " and myArray[2][2] == "x":
            return 1,1
        
        elif myArray[0][0] == " " and myArray[1][1] == "x" and myArray[2][2] == "x":
            return 0,0
            
        elif myArray[0][2] == " " and myArray[1][1] == "x" and myArray[2][0] == "x":
            return 0,2
        
        elif myArray[0][2] == "x" and myArray[1][1] == " " and myArray[2][0] == "x":
            return 1,1
        
        elif myArray[0][2] == "x" and myArray[1][1] == "x" and myArray[2][0] == " ":
            return 2,0
    
        for row in range(0,len(myArray)):
            if myArray[row] == ["o", "o", " "]:
                return row, 2
            
            elif myArray[row] == ["o", " ", "o"]:
                return row, 1
        
            elif myArray[row] == [" ", "o", "o"]:
                return row, 0
            
        #Stops x winning
        for col2 in range(0, len(myArray)):
            newList =[]
            for row2 in range(0, len(myArray)):
                newList.append(myArray[row2][col2])
           
            if newList == ["o", "o", " "]:              
                return 2,col2
            
            elif newList == [" ", "o", "o"]:
                return 0, col2
            
            elif newList == ["o", " ", "o"]:
                return 1, col2
            
        #Stops x winning        
        if myArray[0][0] == "o" and myArray[1][1] == "o" and myArray[2][2] == " ":
            return 2,2
        
        elif myArray[0][0] == "o" and myArray[1][1] == " " and myArray[2][2] == "o":
            return 1,1
        
        elif myArray[0][0] == " " and myArray[1][1] == "o" and myArray[2][2] == "o":
            return 0,0
        
        elif myArray[0][2] == " " and myArray[1][1] == "o" and myArray[2][0] == "o":
            return 0,2
        
        elif myArray[0][2] == "o" and myArray[1][1] == " " and myArray[2][0] == "":
            return 1,1
        
        elif myArray[0][2] == "o" and myArray[1][1] == "o" and myArray[2][0] == " ":
            return 2,0
    else:
        for row3 in range(0,len(myArray)):          #Will place a o in a posistion to win
        
            if myArray[row3] == ["x", "x", " "]:
                return row3, 2
            
            elif myArray[row3] == ["x", " ", "x"]:
                return row3, 1
        
            elif myArray[row3] == [" ", "x", "x"]:
                return row3, 0
            
            for col2 in range(0, len(myArray)): #Will place a o in a posistion to win 
                newList =[]
                for row2 in range(0, len(myArray)):
                    newList.append(myArray[row2][col2])
           
                if newList == ["x", "x", " "]:              
                    return 2,col2
            
                elif newList == [" ", "x", "x"]:
                    return 0, col2
                
                elif newList == ["x", " ", "x"]:
                    return 1, col2
            
        #Will place a o in a posistion to win        
        if myArray[0][0] == "x" and myArray[1][1] == "x" and myArray[2][2] == " ":
            return 2,2
        
        elif myArray[0][0] == "x" and myArray[1][1] == " " and myArray[2][2] == "x":
            return 1,1
        
        elif myArray[0][0] == " " and myArray[1][1] == "x" and myArray[2][2] == "x":
            return 0,0
            
        elif myArray[0][2] == " " and myArray[1][1] == "x" and myArray[2][0] == "x":
            return 0,2
        
        elif myArray[0][2] == "x" and myArray[1][1] == " " and myArray[2][0] == "x":
            return 1,1
        
        elif myArray[0][2] == "x" and myArray[1][1] == "x" and myArray[2][0] == " ":
            return 2,0

def again():
    """ This will ask the user whether they want to do the program again.  """
    programAgain = input(colored("Do you want to do the program again? Y or N: ", "blue"))       #This will ask the user whether they want to re do the program
    
    while programAgain not in ["Y", "y", "yes", "Yes","YES", "No", "NO", "n", "N", "no"]:
        programAgain = input(colored("Do you want to do the program again? Y or N: ", "blue"))
        
    if programAgain in ["Y", "y", "yes", "Yes","YES"]:     #This will check where to go next
        answer = True  #This will then be returned and the menu will be while answer = True
    else:
        answer = False


    return answer
    
def menu():       

    menuOption = input("\nPlease select an option.  \n 1. You to start \n 2. Computer to start \n \n Enter 1 or 2: ")  #This will ask the user which conversion they want to do

    while menuOption not in["1", "2"]:
        menuOption = input("Choose an option.  \n 1. You to start\n 2. Computer to start \n Enter 1 or 2:  ")  #This will ask the user which conversion they want to do
    
    return menuOption
    
def menu2():         
    print(colored("Welcome to Naughts and Crosses/Tic-Tac-Toe.  Please suggest ideas to improve and comment on what you think of it" , "cyan"))
    print(colored("Coming Soon: \nSuggestions Needed", "red"))
    cprint("By Nathaniel Lowis", "blue", "on_white")
    
    menuOption = input("Please select an option.  \n 1. 1 Player Game \n 2. 2 Player Game  \n Enter 1 or 2: ")  #This will ask the user which conversion they want to do

    while menuOption not in["1", "2"]:
        menuOption = input("\nChoose an option.  \n 1. 1 Player Game \n 2. 2 Player Game \n Enter 1 or 2:  ")  #This will ask the user which conversion they want to do
    
    return menuOption
    
def menu3():       

    menuOption = input("\nPlease select an option to choose a difficulty.  \n 1. Easy  \n 2. Medium \n 3. Hard \n Enter 1, 2 or 3: ")  #This will ask the user which conversion they want to do

    while menuOption not in["1", "2", "3"]:
        menuOption = input("\nChoose an option.  \n 1. Easy  \n 2. Medium   \n 3. Hard \n Enter 1, 2 or 3: ")  #This will ask the user which conversion they want to do
    
    return menuOption
    
#main
looper = True
while looper == True:
    
    howManyPlayers = menu2()
    
    if howManyPlayers == "1":
        menuOption = menu()
    
        if menuOption == "2":
            
            difficulty = menu3()
            
            if difficulty == "3":
            
                myArray = [[" " for colindex in range(3)] for rowindex in range(3)]          #Makes a 2d array with nothing in it
                finish = ""
                end1 = 9
                print("\nWelcome to Naughts and Crosses Hard Version.  Your piece is O and you will start second. The row goes from 1- 3 as does columns")
                output_board()
    
                computer_turn2()
                output_board()
            
                while finish != "X" and finish != "O" and end1 != 0:        #Checks if anyone has won   
    
                    your_Turn2()
                    finish = three_In_Row()     #WIll check if it has     finished
                    end1 = any_Spaces()
                    output_board()
                    if finish != "O":
                        if end1 == 9:               #If there are 9 spaces the commputer will go
                            computer_turn2()
                        else:
                            try:            #It will check if it can be strageical
                                rowPos, colPos = computer_turn_strageical2(difficulty)
                                myArray[rowPos][colPos] = "x"
                            except:     #If not it will guess 
                                computer_turn2()
                        finish = three_In_Row()
                        end1 = any_Spaces()
                        output_board()
    
                if finish == "O":   #If person has won will output that
                    print(colored("\nYou have won", "green", attrs=['reverse', 'blink']))
                elif finish == "X":         #If person lost will output that
                    print(colored("\nBetter luck Next time", "blue"))
                elif end1 == 0: #Will print if theres a full board
                    print (colored("\nFull Board", "magenta"))
                    
            elif difficulty == "1":
                
                print("\nWelcome to Naughts and Crosses Easy Version.  Your piece is O and you will start second. The row goes from 1- 3 as does columns")
                myArray = [[" " for colindex in range(3)] for rowindex in range(3)]          #Makes a 2d array with nothing in it
                finish = ""
                end1 = 0
                computer_turn()
                output_board()
                while finish != "X" and finish != "O" and end1 != 0:


                    your_Turn()
                    finish = three_In_Row()
                    if finish != "O":
                        computer_turn()
                        finish = three_In_Row()
                        end1 = any_Spaces()
                    output_board()
    
    
                if finish == "O":   #If person has won will output that
                    print(colored("\nYou have won", "green", attrs=['reverse', 'blink']))
                elif finish == "X":         #If person lost will output that
                    print(colored("\nBetter luck Next time", "blue"))
                elif end1 == 0: #Will print if theres a full board
                    print (colored("\nFull Board", "magenta"))
                    
            else:
            
                myArray = [[" " for colindex in range(3)] for rowindex in range(3)]          #Makes a 2d array with nothing in it
                finish = ""
                end1 = 9
                print("\nWelcome to Naughts and Crosses Medium Version.  Your piece is O and you will start second. The row goes from 1- 3 as does columns")
                output_board()
    
                computer_turn2()
                output_board()
            
                while finish != "X" and finish != "O" and end1 != 0:        #Checks if anyone has won   
    
                    your_Turn2()
                    finish = three_In_Row()     #WIll check if it has     finished
                    end1 = any_Spaces()
                    output_board()
                    if finish != "O":
                        if end1 == 9:               #If there are 9 spaces the commputer will go
                                computer_turn2()
                        else:
                            try:            #It will check if it can be strageical
                                rowPos, colPos = computer_turn_strageical2(difficulty)
                                myArray[rowPos][colPos] = "x"
                            except:     #If not it will guess 
                                computer_turn2()
                        finish = three_In_Row()
                        end1 = any_Spaces()
                    output_board()
    
                if finish == "O":   #If person has won will output that
                    print(colored("You have won", "green", attrs=['reverse', 'blink']))
                elif finish == "X":         #If person lost will output that
                    print(colored("Better luck Next time", "blue"))
                elif end1 == 0: #Will print if theres a full board
                    print(colored("Full Board", "magenta"))
        
        else:
              
            difficulty = menu3()
            
            if difficulty == "3":
        
                myArray = [[" " for colindex in range(3)] for rowindex in range(3)]          #Makes a 2d array with nothing in it
                finish = ""
                end1 = 9
                print("\nWelcome to Naughts and Crosses Hard Version.  Your piece is X and you will start first. The row goes from 1 - 3 as does columns")
                output_board()
    

                while finish != "X" and finish != "O" and end1 != 0:        #Checks if anyone has won   
        
                    your_Turn()#Your go
                    finish = three_In_Row()     #Checks if you have won
                    if finish != "X":
                        if end1 == 9:               #If there are 9 spaces the commputer will go
                           computer_turn()
                        else:
                            try:            #It will check if it can be strageical
                                rowPos, colPos = computer_turn_strageical(difficulty)
                                myArray[rowPos][colPos] = "o"
                            except:     #If not it will guess 
                                computer_turn()
                        finish = three_In_Row()     #WIll check if it has finished
                        end1 = any_Spaces()
                        output_board()
            
                if finish == "X":   #If person has won will output that
                    print(colored("You have won", "green", attrs=['reverse', 'blink']))
                elif finish == "O":         #If person lost will output that
                    print(colored("Better luck Next time", "blue"))
                elif end1 == 0: #Will print if theres a full board
                    print (colored("Full Board", "magenta"))
                    
            elif difficulty == "1":
                
                print("\nWelcome to Naughts and Crosses Easy Version.  Your piece is X and you will start first. The row goes from 1 - 3 as does columns")
                myArray = [[" " for colindex in range(3)] for rowindex in range(3)]          #Makes a 2d array with nothing in it
                finish = ""
                end1 = 9
                output_board()
                while finish != "X" and finish != "O" and end1 != 0:


                    your_Turn()
                    finish = three_In_Row()
                    if finish != "X":
                        computer_turn()
                        finish = three_In_Row()
                        end1 = any_Spaces()
                        output_board()
    
    
                if finish == "X":   #If person has won will output that
                    print(colored("You have won", "green", attrs=['reverse', 'blink']))
                elif finish == "O":         #If person lost will output that
                    print(colored("Better luck Next time", "blue"))
                elif end1 == 0: #Will print if theres a full board
                    print (colored("Full Board", "magenta"))  
                    
            else:
        
                myArray = [[" " for colindex in range(3)] for rowindex in range(3)]          #Makes a 2d array with nothing in it
                finish = ""
                end1 = 9
                print("\nWelcome to Naughts and Crosses Medium Version.  Your piece is X and you will start first. The row goes from 1 - 3 as does columns")
                output_board()
    

                while finish != "X" and finish != "O" and end1 != 0:        #Checks if anyone has won   
        
                    your_Turn()#Your go
                    finish = three_In_Row()     #Checks if you have won
                    if finish != "X":
                        if end1 == 9:               #If there are 9 spaces the commputer will go
                            computer_turn()
                        else:
                            try:            #It will check if it can be strageical
                                rowPos, colPos = computer_turn_strageical(difficulty)
                                myArray[rowPos][colPos] = "o"
                            except:     #If not it will guess 
                                computer_turn()
                        finish = three_In_Row()     #WIll check if it has finished
                        end1 = any_Spaces()
                        output_board()
            
                if finish == "X":   #If person has won will output that
                    print(colored("You have won", "green", attrs=['reverse', 'blink']))
                elif finish == "O":         #If person lost will output that
                    print(colored("Better luck Next time", "blue"))
                elif end1 == 0: #Will print if theres a full board
                    print (colored("Full Board", "magenta"))
        
    else:
        #main
        myArray = [[" " for colindex in range(3)] for rowindex in range(3)]          #Makes a 2d array with nothing in it
        finish = ""
        end1 = 9
        print("\nWelcome to Naughts and Crosses.  Player 1 is x and Player 2 is o. The row goes from 1 - 3 as does columns")
        output_board()

        while finish != "X" and finish != "O" and end1 != 0:
            print("Player 1")
            your_Turn()
            finish = three_In_Row()
            end1 = any_Spaces()
            output_board()
            if finish != "X" and finish != "O" and end1 != 0:
                print("Player 2")
                your_Turn2()
                finish = three_In_Row()
                end1 = any_Spaces()
                output_board()

        if finish == "O":   #If person has won will output that
            print(colored("Player 2 has won", "green", attrs=['reverse', 'blink']))
        
        elif finish == "X":         #If person lost will output that
            print(colored("Player 1 has won", "blue"))
            
        elif end1 == 0: #Will print if theres a full board
            print (colored("Full Board", "magenta"))
            
    looper = again()
