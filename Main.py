import random
from colorama import Fore, Style, init

init()

#List of words
easy_words=["apple","chair","book","cafe","tiger","game","music"]

medium_words=["laptop","village","friend","cabbage","giraffe","bottle","biscuit"]

hard_words = ["education","entertainment","politics","country","health",
"calendar","kingdom"]

#Hangman Art
hangman_stages=[
    """
      -----
      |   |
          | 
          |
          |
          |
    =======

""",
    """
      -----
      |   |
      O   |
          |
          |
          |
    =======

""",
"""
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =======

""",
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =======

""",
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =======

""",
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =======

""",

]

# Choose random word based on difficulty
def choose_word():

    print(Fore.BLUE+ "=" * 40+ Style.RESET_ALL)
    print(Fore.BLUE+ "🎮 WELCOME TO HANGMAN 🎮"+ Style.RESET_ALL)
    print(Fore.BLUE+ "=" * 40+ Style.RESET_ALL)

    print("\nChoose Difficulty:")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")

    choice=input("\nEnter your choice (1/2/3):")

    if choice=="1":
        return random.choice(easy_words),6
    elif choice=="2":
        return random.choice(medium_words),5
    else :
        return random.choice(hard_words),4
    
   #Displaying the word with guessed letters
def display_game(chosen_word, guessed_letters, attempts):
    
    stage_index = len(hangman_stages) -1 -attempts

    if stage_index <0:
        stage_index=0

    print(hangman_stages[stage_index])

    display_word=""
    
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word+=letter+""
        else:
            display_word+="_"
    print("\nWord: ", display_word)
    print("Guessed letters: ",guessed_letters)
    print("Remaining Attempts: ",attempts)

    return display_word

    # Validating the input
def  get_guess():

    while True:

        guess=input("\nGuess a letter: ").lower()

        if len(guess) !=1 or not  guess.isalpha():
           print("⚠️ Please enter a single letter")
        else:
            return guess

 #Playing the game   
def play_game():

    chosen_word, attempts=choose_word()

    guessed_letters=[]

    while attempts>0:

        display_word=display_game(
            chosen_word,guessed_letters,attempts
        )
              #If the user has won
        if "_" not in display_word:
            print(Fore.GREEN +"\n🎉 Congratulations! You won!"+ Style.RESET_ALL)
            break
            #If the letter was already guessed
        guess=get_guess()

        if guess in guessed_letters:
            print(Fore.LIGHTYELLOW_EX +"⚠️ You already guessed that letter!"+ Style.RESET_ALL)
            continue

        guessed_letters.append(guess)

               #Wrong guess
        if guess not in chosen_word:
            attempts-=1
            print(Fore.LIGHTRED_EX +"❌ Wrong guess!"+ Style.RESET_ALL)

          #If the user loses
        if attempts==0:
            print(hangman_stages[6])
            print(Fore.RED +"\n💀 Game Over!"+ Style.RESET_ALL)
            print("The word was: ",chosen_word)

#Start Game

while True:
    play_game()

    replay=input("\nDo you wanna play again? (y/n): ").lower()

    if replay != "y":
        print("Thanks for playing 👋")
        break
