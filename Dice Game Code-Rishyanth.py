

# Dice Game
# User Authentication
import time
print("""
--------------------------------------------------
-- ----   ------------------------------  ----- --
          ====   ======  ======  ======= 
          =  =     ==    ==      =
          =   =    ==    =       ======
          =   =    ==    =       ======
          =   =    ==    ==      =
          ====   ======  ======  =======    
-- -----  ------------------------------  -----  --
-- -----  ------------------------------  -----  -- """)
print("""
                                          
                                          =============
                                       =  ==         ==
                                      =   ==    .    ==
                                      =   ==         ==
                                      = . ==         ==
                                      =   =============
                                      =  =           =
                                      = =           =
                                       =============
                                      """)
                                          
def Start():                                       # Start function allows the user to login or register based on their choice
    print("----------------Welcome  to DROP DEAD ---------------------")
    print("\n")
    print("Are you a new user ? Y or N ")       
    ch=str(input("Please choose an option: ")) # Variable choice asks the user to login or register
    choice=ch.upper()
    
    if choice == "Y":
        Register()                                 # Allows the user to register if their choice is Yes
    elif choice == "N":
        Login()                                    # Allows the user to login if their choice is No
    else:
      print("\n")
      print("Please enter a valid option ( Y or N )")
      print("\n")
      Start()                                     # Takes the user back to the start menu if their choice is invalid.

      

# Function register allows the user to create and account and stores it in the UserDetails text file.

def Register ():

    # Allows the user to input personal details
    
    global name
    
    name=str(input("Please enter your first name: "))      
    name=name.capitalize()
    
    age=int(input("Please enter your age (AA) : "))
    age=str(age)
    
    import random      
    number=random.randint(1,10)
    number=str(number)
    global username
    username = name[:3] + age[:2] + number   # Randomly Generates a username based on their name and age 
    print("\n")
    print(" Your username is",username)
    print("\n")
       
    password=str(input( "Create a password: ")) # Allows the user to create a password
      

  # Amends the name, username and password of the player to the text file ( playerDetails.txt )
 
    file=open("playerDetails.txt","a")
        
    """file.write (name)
    file.write (",")"""
    file.write (username)
    file.write (",")
    file.write (password)
    file.write ("\n")
    
    print("Account Created!")

    file.close()    # Saves the text file.



# Function Login allows the player to login to the game by enetering their username and password if they are already an user
            
def Login():
  
    print('-------------Welcome to the login page----------------')
    
    
    username=input('username: ')    # Asks the user to input username   
    password=input('Password: ')    # Asks the user to input password

    """file=open("playerDetails.txt","r")
    fRead=file.readlines()
    for lines in fRead:
        line=lines.split(",")
        if username==line[1] and password==line[2]:
            print("Correct Credentials!")
            break
    else:
        print("Inccrrect Credentials")
        Start()"""

        
    file=open("playerDetails.txt","r")
    file.seek(0)
    lines=file.readlines()
    for line in lines:
        line=line.strip()
        words=line.split(",")
        
        if username==words[1] and password==words[2]:
            print("Login Successfull")
            
            global name
            name=words[0]
            break
    else:
        print("Incorrect Credentials")
        Start()            

   
        
       
               
username=str()       # Variable username assigned outside the function to delcare a global variable

print("\n")                       
print (" PLAYER 1 ") 
print("\n")                        
Start()

player1username=username  # Assigns the username of the first player as Player 1 username
player1Name=name          # Assings the name of the first player as Player 1 Name 


print("\n")
time.sleep(1)
print ( " PLAYER 2 ")
print("\n")
Start()
print("\n")

player2Name=name          # Assigns the username of the first player as Player 2 username      
player2username=username  # Assings the name of the first player as Player 2 Name 


print("\n")
time.sleep(2)
print("""
 
 ==      ======   =======  ======    ======  ======  =======   ======   ===  =   ==
 ==      ==         ==     ==        =    =  ==      =           =      = =  =   ==
 ==      ======     ==       ====    =====   ======  =    ==     =      =  = =   ==
 ==      ==         ==        ====   =    =  ==      ===  ==     =      =   ==   
 ======  ======     ==     =====     ======  ======   =====    ======   =    =   ..
                                                                                 ..
""") 
print("\n")
time.sleep(1)
print("""
      ======================================================== RULES =========================================================
   =                                                                                                                           =
   =  1. The games includes 5 rounds                                                                                           =
   =  2. Each player gets a chance to roll the dice twice in each round                                                        =
   =  3. The dice number is added to the player's score                                                                        =
   =  4. If the two dice numbers are equal the player gets to roll an extra dice                                               =
   =  5. If the player rolls an even number, an extra 10 points are added.                                                     =
   =  6. If the player rolls an odd number, 5 points are removed from their score                                              =
   =  7. The person with the highest score at the end of round 5 wins                                                          =
   =  8. if the score at the end of round 5 of both the plaayers are equal, they get to roll the dice until one of them wins   =
   =                                                                                                                           =
      ========================================================================================================================  """)
   


def diceNumber ():    # Imports a random number between 1 and 6 
   
     import random
     global diceScore
     diceScore=random.randint(1,6)
     print("Your Dice Score is",diceScore)
     global Score             # Gloabl Varibale Socre
     Score=Score+diceScore    # Adds the dice score to the total score
     Dice=diceScore%2
     if Dice==0:
       print("Its an EVEN number!")  # if the dice score is an even number adds additional 10 points
       Score=Score+10
       
       print("Your current score in this round is",Score)  # Outputs the currect score in the round 
     else:
       print("Its an ODD number!")  # If the dice scor eis an odd number it takes away 5 points from the total score
       Score=Score - 5
       if Score<0:
         Score=0    # makes sure that the player's score is not below 0 
       print("Your score at the end of round",Round,"is",Score)


#  variables that are declared as global variables to be used within and outside the function

name=str()
diceScore=int()
Round=int()
Round=1
Score=0
player1Score=int()
player2Score=int()
Winner=str()
WinnerScore=str()
diceWinner=str()

  
def Player1 ():          # Allows Player 1 to roll the dice twice in each round        
    
    print("\n")
    print("-------------------")
    print("WELCOME TO ROUND", Round)
    print("\n")
    print("Player 1, you play first")
    print("\n")
    
    print("Press ENTER to Start\n")
    Enter=input()
    print("Are you ready!\n")
    time.sleep(1)
    print("Lets roll the dice!....3...2...1..begin!")
    time.sleep(1)
    
    print("\n")

    global player1Score
    diceNumber()        # Defines the DiceNumber function to add the dice score to player 1 score in eavery round
    diceNumber1 = diceScore
    print("Press ENTER to roll the dice")
    ENTER=input()
    diceNumber()       # Rolls the dice twice
    diceNumber2 = diceScore  
    if diceNumber1 == diceNumber2:     # Allows the user to roll a double if the to dice numbers are equal.
      print("\n")
      time.sleep(1)
      print("You got a DOUBLE!!!")
      print("Press ENTER to roll the dice")
      ENTER=input()
      diceNumber()
    



    player1Score=Score

def Player2 ():
    print("\n")
    time.sleep(1)
    print("Player 2 its your turn")
    print("\n")
    
    print("Press ENTER to start\n")
    enter=input()
    
      
    print("Are you ready!")
    print("\n")
    time.sleep(1)
    
    print("Lets roll the dice!....3...2...1..begin!")
    print("\n")
    time.sleep(1)
    
    global player2Score
    diceNumber()
    diceNumber1 = diceScore
    print("\n")
    print("Press ENTER to roll the dice")
    ENTER=input()
    
    diceNumber()
    diceNumber2 = diceScore
    if diceNumber1 == diceNumber2:
      print("\n")
      time.sleep(1)
      print("You got a DOUBLE!!!")
      diceNumber()
    player2Score=Score

  

def Winners ():
  global Round

number=int()
def DiceRoll():
  import random
  global number
  number=random.randint(1,6)
  print("Your Dice Score is",number)
  

while Round<=5:
  Player1()
  diceScore=0
  time.sleep(2)
  Player2()
  
  print("\n")
  choice=str(input("PRESS ENTER TO MOVE TO THE NEXT ROUND......!!!"))
  Round=Round+1
  Winners()

def Leaderboard():
    
    import mysql.connector as sqltor   # Imports database programming package
    mycon=sqltor.connect(host="localhost",user="root",passwd="DbDice",database="DropDead")
    # Establishes connecton with the database dropdead stored in mysql
    mycursor=mycon.cursor()   #  Creates a cursor instance that is used to execute queries on the database
    
    query="insert into Leaderboard(Name,Score) values('{}',{})".format(Winner,WinnerScore)
    # Inserts the Winner's name,score in the table Leaderboard 
    mycursor.execute(query)  # Query executed 
    mycon.commit()
    # Permanent changes made to the table
    
    query2="select * from Leaderboard order by score desc"
    # Selects all the rows from the table Leaderboard in descending order of the Winnsers' scores
    mycursor.execute(query2)
    
    data=mycursor.fetchmany(5)  # Retreives 5 rows from the resultset 
    for row in data:
        print(row)  # Outputs the top 5 highest scorers of all time 
    mycon.close()   # Cleans up the environment 
    




def Verification():

  if player1Score > player2Score:
      
      global player1Name
      print(player1Name,"(Player 1) Wins !")
      print("Well Done")
      time.sleep(1)
      print("Processing........\n")
      time.sleep(1)
      
      print("Don't miss out the LEADERBOARD !")
      LB=input()
      print("\n")
      print('   These are our Top 5 scorers ')
      print("""
   =     =====     =      =====  ====  =====  =====   ===      =      =====    =====
   =     =        ==      =    = =     =   =  =   =  =   =    ===     =   =    =    =
   =     ====    = = =    =    = ===   = =    ====   =   =   =====    = = =    =    =
   =     =      =     =   =    = =     =   =  =   =  =   =  =      =  =    =   =    =
   ====  ===== =       =  =====  ====  =    = === =   ===   =      =  =     =  =====
   """)
      global Winner
      Winner=player1Name
    
      global WinnerScore
      WinnerScore=str(player1Score)       
      
      Leaderboard()
      
      
      

  elif player2Score > player1Score:
      global player2Name
      print(player2Name,"(Player 2 )Wins !")
      print("Well Done")
      time.sleep(1)
      print("Processing...........................\n")
      time.sleep(1)
      print("Don't miss out the LEADERBOARD !")
      print("Press ENTER to open the Leaderboard")
      LB=input()
      print("\n")
      print('---------THESE ARE OUR TO 5 SCORERS---------- ')
      print("""
   =     =====     =      =====  ====  =====  =====   ===      =      =====    =====
   =     =        ==      =    = =     =   =  =   =  =   =    ===     =   =    =    =
   =     ====    = = =    =    = ===   = =    ====   =   =   =====    = = =    =    =
   =     =      =     =   =    = =     =   =  =   =  =   =  =      =  =    =   =    =
   ====  ===== =       =  =====  ====  =    = = = =   ===   =      =  =     =  =====
   """)
      
      Winner=player2Name
      WinnerScore=str(player1Score)
      
      
      Leaderboard()
      
      

  elif player1Score==player2Score:

      print("Your scores are equal")
      print("\n")
      print("Both of you will roll the dice again")
      print("\n")
      print("Player 1, your turn")
      print("\n")
      print(" Are you ready!")
      print("Lets roll the dice!....3...2...1..begin!")
      print("\n")
      DiceRoll()
      Player1=number
      print("Player 2, your turn")
      print("\n")
      print(" Are you ready!")
      print("Lets roll the dice!....3...2...1..begin!")
      print("\n")
      DiceRoll()
      Player2=number
      if Player2==Player1:
        Winners()

  


if Round==6:

    print("\n")
    print("Processing.................................")
    print("\n")
    print("Waiting to display the winner.............. ")
    print("Player 1, your score is",player1Score)
    print("\n")
    print("Player 2, your score is,",player2Score)
    Verification() 




