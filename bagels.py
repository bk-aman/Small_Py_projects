import random

NUM_DIGIT = 2 
MAX_GUESSES = 10

def getSecretNum():
    """ Generate 3 digit random number as secret number : a generalised program to generate N digit random number
    """
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNumber = ''
    for i in range(NUM_DIGIT):
        secretNumber += numbers[i]
    return secretNumber

def getClues(guess, secretNumber):
    ''' Generate Clues for guesse
    '''
    guess = str(guess)
    if guess == secretNumber:
        print('You have guessed number RIGHT!!')

    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            # A correct digit in correct place
            clues.append('Fermi')
        elif guess[i] in secretNumber:
            # A correct digit in incorrect place
            clues.append('Pico')

    if len(clues) == 0:
        #None matches
        return 'Bagels'    
    else:
        clues.sort() #sorting it so that order cant be known
        return (' ').join(clues)


def main():
    print(f""" Bagels a deductive logic game,

          I am thinking of a {NUM_DIGIT} digit number with no repeated digits.
          Try to guess what it is. Here are some clues.
          
          When I say       It means
          Pico             One digit is correct, but in wrong position.
          Fermi            One digit is correct and in right position. 
          Bagels           No digit in correct position.

          for example if number is 248 and you guessed 843, the clues will be Fermi and Pico
          """)
    
    #main loop here
    while True:
        secretNumber = getSecretNum()
        # print(secretNumber)
        print(f"""
                I have thought of Number.
                You have {MAX_GUESSES} to guess it
              """)
        
        numGuess = 1
               
        while numGuess <= MAX_GUESSES:
            # print(number)
            guess = ''
            #keep looping untill a valid guess
            while len(guess) != NUM_DIGIT or not guess.isdecimal():
                print(f'Guess #{numGuess}')
                guess = input('> ')
            
            clues = getClues(guess, secretNumber)
            print(clues)

            numGuess += 1

            if guess == secretNumber:
                print('Congratulations ypu have guessed the number right')
                break

            if numGuess > MAX_GUESSES:
                print('You ran out of Guesses')
                print(f'The answer was {secretNumber}')
            
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
               break
    print('Thanks for playing')


if __name__ == '__main__':
    main()



        



        
        