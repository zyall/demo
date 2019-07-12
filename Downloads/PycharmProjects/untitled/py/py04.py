#！／usr/bin/env python3
#coding=utf-8

import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words='ada ruby python java groovy elixir basic sharp swift rails'.split()
#从list随机返回一项
#random.choice()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList) - 1)
    return wordList[wordIndex]
def dispalyBoard(HANGMANPICS, missedLetters,correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Missed letters: ')
    tmp=''
    for letter in missedLetters:
        tmp = tmp + letter + ''
        #print('%s' %letter)
    print(tmp)

    blanks ='_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i] + secretWord[i] + blanks[i+1:]
    tmp=''
    for letter in blanks:
        tmp =tmp + letter + ''
    print(tmp)
    print()
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess=input()
        guess=guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'adcdefghijklmnopqrstuvwxyz' :
            print('Please enter a LETTER.')
        else:
            return guess
def playAgain():
    print('Do you want to play again?(yes or no)')
    return  input().lower().startswith('y')

print('H A N G M A N')


missedLetters=''
correctLetters=''
secretWord=getRandomWord(words)
gameIsDone=False
while True:
    dispalyBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    guess=getGuess(missedLetters+correctLetters)
    if guess in secretWord:
        correctLetters=correctLetters + guess
    foundALLLetters=True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundALLLetters=False
            break
    if foundALLLetters:
        print('Yes! The secret word is "'+ secretWord +'"! You have won!')
        gameIsDone=True
    else:
        missedLetters=missedLetters+guess
        if len(missedLetters)== len(HANGMANPICS) -1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
        print('You have run out of guesses!\nAfter '+ str(len(missedLetters))+' missed guesses and '
        + str(len(correctLetters))+' correct guesses, the word was "'+secretWord +'"')
        gameIsDone=True
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone=False
            secretWord=getRandomWord(words)
        else:
            break












