import random
from os import system, name
# Clean the screen everytime the game is started
def clean_screen():
    if name == 'nt':
        _= system('cls') #Windows 
    else:
        _=system('clear') #Linux or MacOS
        
def game():
    clean_screen()
    print("\nWelcome to the guessing game called Hangman!")
    print("Guess the word below, the theme is: Animals")
    
    # Avaiable words in the game
    animals = ['wolf', 'turtle', 'dog', 'whale', 'ostrich', 'owl', 'beaver']
    
    # Randomically one word is chosen
    animal = random.choice(animals)
    
    # Calculate how many underscores should we have
    underscores = ['_' for word in animal]
    
    # Number of chances
    chances = len(underscores) + 2
    
    # List for all the wrong letters
    wrong_ones = []
    
    while chances > 0:
        
        print(" ".join(underscores))
        print("\nHow many chances you have:", chances)
        print("Wrong letters:", " ".join(wrong_ones))
        
        attempt = input("\nType a letter: ").lower()
        
        #Fill 
        if attempt in animal:
            for index, letter in enumerate(animal):
                if attempt == letter:
                    underscores[index] = attempt
        else:
            chances -= 1 
            wrong_ones.append(attempt)
        
        if "_" not in underscores:
            print("\nCongratulations, You win! The word was:", animal)
            break
    if "_" in underscores:
        print("\nYou loose, the word was: ", animal)

if __name__ == "__main__":
    game()
    print("\nMade with Data Science Academy")

