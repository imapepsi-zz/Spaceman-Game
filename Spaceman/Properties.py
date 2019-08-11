#Start
#Secret word library, drawing list (Strings)

#Drawings
SPACEMANDRAWINGS = ["""
    

        O   
       /|\  
       / \  
     """, """
      _____ 
     /     \      
    
   
    
        O   
       /|\  
       / \ 
     """, """
      _____ 
    _/_____\_   
  
  
    
        O   
       /|\  
       / \  
     """, """
      _____     
    _/_____\_       
     \_____/        
          
        
        O   
       /|\  
       / \  
     """, """
      _____ 
    _/_____\_   
     \_____/    
     /     \        
    /       \   
        O   
       /|\  
       / \  
     """, """ 
      _____ 
    _/_____\_   
     \_____/    
     /  O  \    
    /  /|\  \ 
       / \     

        
     """, """ 
      _____ 
    _/_____\_ 
     \_____/ 
     /     \ 
    /       \  
    
     

    """, """
      _____ 
    _/_____\_ 
     \_____/ 
          
    
    
    

    """]


#Word Library
wordList = """scale head zipper land edge hands office mask development chairs
leather canvas channel religion surprise throne goose mass ear box cart beetle help
breakfast lunch dinner snack popcorn phone audio superhero note letter keyboard
moniter computer laptop cars summer winter fall spring carpenter suggestion
dog cat fish tiger lion kola kangaroo elephant kite afternoon morning evening night
channel birth boat cup needle ducks apparel books zephyr fowl soccer tennis basketball 
donut flower burger newspaper space skyscraper window behavior""".split()

def displayBoard(correct, missed, secret):
    """Disply a Spaceman Drawing, missed Letters, correct letters, and secret word"""
    
    currentDraw = SPACEMANDRAWINGS[len(missed)] #Missing = string of incorrect leters
    
    print(currentDraw)
    print("Letters Missed:", end=" ")
    for c in missed:
        print(c, end=" ")
    print("")

    blanks = "_ " * len(secret)
    for c in range(len(secret)):
        if secret[c] in correct: #if the letter at this secret index is in the list of correct letters
            blanks = blanks[:c*2] + secret[c] +" "+ blanks[(c*2):-2] #create blanks till the index of the correct letter place
                                                            #the correct letter, then create blanks till the end
    print("Secret Word: {}".format(blanks))
    print("")

def getGuess(alreadyGuessed):
    """Gets a player's guess and checks if it's valid"""
    while True:
        guess = input("Guess a Letter: ").lower() #Lower case any input
        
        if len(guess) != 1:
            print("Only One character at a time."+"\n")
        elif guess in alreadyGuessed:
            print("You already guessed this letter."+"\n")
        elif guess not in "abcdefghijklmnopqrstuvwxyz": #Check if in alphabet
            print("Please enter a letter from the English Alphabet."+"\n")
        else:
            break
        
    return guess

def checkGuess(guess, correct, missed, secret):
    if guess in secret:
        correct += guess #Place guess in correct if correct
    else:
        missed += guess #Place guess in missed if incorrect
    
    return correct, missed

def checkWin(correct, missed, secret):
    """Check if a Player has won"""
    status = "Win"
    if len(missed) == len(SPACEMANDRAWINGS):
        status = "Lost"
    else:
        for i in range(len(secret)):
            if secret[i] not in correct:
                status = "Playing"
                break
    return status



def playAgain():
    answer = input("Do you want to play again? (yes or no) ").lower()
    return answer

