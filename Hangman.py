#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# python program
# Hangman game

import random
from collections import Counter

Some_Words = ''' apple banana cheery gauva orange papaya watermelon grapes mango lichi pineapple lemon '''
Some_Words = Some_Words.split(' ')

      # randomly choose secret word from "Some_Words" List

word = random.choice(Some_Words)

if __name__ == '__main__':
    print('Guess The Word! Hint ? It is the name of fruits')
    
    for i in word:
        
        print('_', end = ' ')
    print()
    
    plyng = True
    
    # list for storing the letters which gussed by player
    
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0


    try:
        while ( chances != 0 ):
            print()
            chances -= 1
        
            try:
                 Guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only letter! ')
                continue
        
            if not Guess.isalpha():
                print('Enter only a letter ')
                continue
            elif len(Guess) > 1:
                print(' Enter only single letter: ')
                continue
            elif Guess in letterGuessed:
                print('you have already guessed that letter ')
                continue
    
            if Guess in word:
                letterGuessed += Guess
    
# Print word
            for char in word:
                if char in letterGuessed:
                     print(char, end = ' ')
                     correct += 1
                else:
                    print('_', end = ' ')
        
    # If user has guessed all the letters 
            if(Counter(letterGuessed) == Counter(word)):
                print() 
                print('Congratulations, You won!') 
                break
         # If user has used all of his chances
        if chances == 0 :
             print()
             print('You lost! Try again..')
             print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print() 
        print('Bye! Try again.') 
        exit() 
  
        # print(letterGuessed) 


# In[ ]:




