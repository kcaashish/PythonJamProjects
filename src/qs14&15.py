import random


def guessingGame():
    global userInput
    N = random.randint(1, 100)
    print("Guess the integer number, you will have 5 tries: ")
    count = 0
    running = True

    while running:
        takeInput = True
        while takeInput:
            try:
                userInput = int(input())
                assert 1 <= userInput <= 100
                takeInput = False
            except AssertionError:
                print("Enter a value between 1 and 100: ")
                takeInput = True

        count += 1

        if userInput < N:
            print("Enter a larger number! ")
        elif userInput > N:
            print("Enter a smaller number!")
        else:
            print("You have won!")
            print("You have won in " + str(count) + " tries.")
            running = False
            return 0

        if count == 5:
            print("Maximum attempts reached!")
            running = False
            return 0

        print("Tries remaining:{}".format(5 - count))


guessingGame()
