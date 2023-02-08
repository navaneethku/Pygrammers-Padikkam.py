import random
num = random.randint(1,10)
while(True):
    print("\nGuess number between 1 and 10")
    choice = int(input())
    print(f"\nYour entered choice is : {choice}")
    if(choice == num):
        print("Congrats!, your guess is correct!")
        break;
    else:
        print("\nWrong Guess :(\nTry Again!")