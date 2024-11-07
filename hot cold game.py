import random

unknown = random.randint(1,100)
count = 0

print("Hot Cold Game")
print("---------------------------\n")
print("Lets guess a number (1-100)")

while True:
    guess = float(input("Your guess: "))

    if not guess.is_integer():
        print("! Please enter an integer !\n")

    elif guess < 1 or guess > 100:
        print("! Please enter a number between 1 and 100 !\n")

    else:
        count = count+1

        if guess == unknown:
            print(f"You found it on the {count}. try! the secret number was {int(guess)}\n")
            break
        else:
            if guess > unknown and guess - unknown > 20 or unknown > guess and unknown - guess > 20:
                print("cold\n")
            elif guess > unknown and guess - unknown > 10 or unknown > guess and unknown - guess > 10:
                print("warm\n")
            else:
                print("hot\n")