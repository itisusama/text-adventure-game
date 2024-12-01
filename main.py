import time
import math
import random

classTypes = ["Mage", "Barbarian", "Archer", "Bonk Person"]
statNames =  ["Attack", "Speed", "Defence", "Special Power", "Health"]
classStats = [[3,5,5,10,100],[10,7,3,3,100],[7,10,5,1,100],[5,6,5,6,100]]
playerName = ""
playerStats = [0,0,0,0,0]
statAdjustment = [0,0,0,0,0]
playerClass = -1 
playerMoney = 500
playerStatus = "Fine"
PlayerLevel = 0
playerExperience = 0
currentLocation = "Home"
placesToTravel = [["Oodragoth", "CastleVania", "MilkTown", "Home"],[200,300,75,0]]
distanceToHome = 0
activityMenu = ["View Stats", "Travel", "Shop", "Inventory"]
itemsToBuy = [["potion", "burnHeal", "iceHeal", "statBoost", "cheapVase", "expensiveVase", "garbage"], [100,50,50,200,25,300,0]]
inventory = ["potion"]

def indexInList(item, myList):
    foundIndex = -1
    for i in range(len(myList)):
        if(item == myList[i]):
            foundIndex = i
            break
        return foundIndex
    
def listToText(myList):
    combinedText = "\n"
    for i in range(len(myList)):
        combinedText += str(i) + ": " + myList[i] + "\n"
    return combinedText + "\n"

def checkMenuRange(question, listName, isCancelable = False):
    index = int(input(question + listToText(listName)))
    while(True):
        if(isCancelable and index == -1):
            return index
        elif index < 0 or index > len(listName) -1:
            index = int(input("Invalid choice please try again\n"))
        else:
            return index
        
def lineBreak(numRows, numSleep):
    line = "*" * 18
    for i in range(numRows):
        print(line)
    time.sleep(numSleep)
    
playerName = input("What is your name\n")
print(f'Welcome to the game {playerName}!')
lineBreak(2,1)
for i in range(len(classTypes)):
    lineBreak(1,1)
    print(classTypes[i])
    lineBreak(1,1)
    for j in range(len(classStats[i])):
        print(f'{statNames[j]}: {classStats[i][j]} \n')
playerClass = checkMenuRange("Choose your Class:", classTypes)
print(f'You have chosen {classTypes[playerClass]}!')
playerStats = classStats[playerClass]
lineBreak(2,2)
print(f'From henseforth you shall be known as {playerName} the {classTypes[playerClass]}')
lineBreak(1,3)
print("Long ago in a time when anything was possible there was a land called HOME\n that was ironically home to a great warrior\n but spooky things.")
lineBreak(1,6)