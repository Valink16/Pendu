#Writed by: Valink, on: 27.11.2017

from func import loadFile, prtDebug, createMask
from random import randint

wordList=loadFile("wordList")["content"]
wordTab=wordList.split("\n") #Separating wordList into a tab
wordToGuess=list(wordTab[randint(0, len(wordTab)-1)]) #Getting a random word and turning it into a list
wordMask=createMask(wordToGuess) #Setting up mask used to track player's progression

playing=True
#prtDebug(str(wordToGuess))

print("".join(wordMask))
while playing==True: #Main game loop
    l=input("Entrez une lettre: ")

    while(True): #To validate multiple letters at a time if l is in the wordToGuess multiple times
        if l in wordToGuess: #Checking if l is in the word and changing wordMask
            lIndex=wordToGuess.index(l)
            wordToGuess[lIndex]="*"
            wordMask[lIndex]=l
        else:
            break

    if not("*" in wordMask): #If there's no more "*" in wordMask that means the player found the word
        print("Vous avez gagné, Bravo !")
        playing=False

    print("".join(wordMask))
