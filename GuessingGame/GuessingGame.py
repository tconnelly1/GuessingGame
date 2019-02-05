'''
Created on Jan 28, 2019

@author: Tom
'''
import random


def guessingGame():
    #Initialize the random number
    theNumber = random.randint(1,101)
    userIn = None #initialize the user input variable
    n = 0 #initialize counter variable
    while userIn!=theNumber:    #run loop to repeat input prompt
        try:
            n = n + 1 #add 1 to counter for each input
            userIn = int(input("I'm thinking of a number between 1 and 100. Try to guess the number I'm thinking of: "))
        except: TypeError("\nYou must enter a number!") #error message based on type exception
        if userIn >= 1 and userIn <= 100: #check to see if user input is in range
            if userIn == theNumber:
                print("\nYou're right! Good job!")
                print("\nIt took you", n, "guesses") #print success statement and amount of guesses
                return #return None and end the function
    
            elif userIn < theNumber: #check user input vs theNumber. Gives clue that input is too low
                print("\nToo low. Guess again\n")
            elif userIn > theNumber: #check user input vs theNumber. Gives clue that input is too high
                print("\nToo high. Guess again\n")  
        elif userIn<1 or userIn>100: #statement for if the user input is outside of the range
            print("\nThe number must be between 1 and 100!") #error message if user input is outside of the range          

if __name__ == "__main__":
    guessingGame()