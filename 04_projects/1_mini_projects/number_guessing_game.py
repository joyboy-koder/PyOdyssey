# random
# while loop
# conditionals
import random


guess = random.randint(50,101)

def main():
    global guess
    while True:
        num = int(input("Guess a number between 50 and 100: "))
        if num == guess:
            print('Wohoo!, youre right on your guess!')
            break
        elif num < guess:
            print("Go a little higher on your guess!")
        else:
            print("Go a little lower on your guess!")
main()