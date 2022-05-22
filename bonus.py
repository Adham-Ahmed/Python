# not the cleanest code the sole purpose is getting familiar with the syntax
from pickle import FALSE, TRUE
import random

def randomNumberFrom0To100():
    return random.randint(0,100)

def check_valid_number(inputNumber):
        if(inputNumber <0 or inputNumber >100):
            print(
                """number should be between 0 and 100 this does not
                count as a try."""
            )
            return 0
        else:
            return 1

def checkIfEnteredBefore(inputNumber,entered_numbers):
    if(inputNumber in entered_numbers):
        print(
        """number has been entered before, this does not
        count as a try."""
             )
        return 1
    else:
        # entered_numbers.append(inputNumber)
        return 0

def WinningMsg(inputNumber,randomNumberFrom0To100):
    if(inputNumber == randomNumberFrom0To100):
        print("Congratulations you won !")
        # break;
        return 1
    else:
        return 0


def Game():
    entered_numbers=[];
    tries=10;
    randomNumber=randomNumberFrom0To100()
    entered_numbers=[]
    while(tries>0):
        inputNumber=int(input("Enter Your Number:")); 
        isValid=check_valid_number(inputNumber)
        HasbeenEntered=checkIfEnteredBefore(inputNumber,entered_numbers)

        if(isValid and not HasbeenEntered):
            entered_numbers.append(inputNumber)
            tries=tries-1;

        won=WinningMsg(inputNumber,randomNumber)
        if won:
            break;


    if (tries == 0 or won ):
        WantToPlay=input("do you want to play again Y/N?")
        if(WantToPlay=="Y" or WantToPlay=="y"):
            Game();
Game()



   
        
    

