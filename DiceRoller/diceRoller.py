import random
while(True):
    print("\nDo you want to roll the dice?\nYes : y | Y\nNo : n | N")
    choice = input()
    if(choice == 'y' or choice == 'Y'):
        print("The dice landed on : " + str(random.randint(1,6)))
    elif(choice == 'n' or choice == 'N'):
        print("Thank you for using my diceRoller program!")
        break;
    else:
        print("Invalid Option!")
        
         