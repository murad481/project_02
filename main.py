'''
We are going to write a program that generates a random number and
ask the user to guess it.
If The player's guess is higher than the actual number, the program 
displays "Lower number please". Similarly, if the users's guess us
too low, the program prints "higher number please" when the user 
guesses the correct numbe, the program displays the number of guesses
the player used to arrive at the number.

Hint: Use the random module.
'''

import random

# Step 1: Generate a random number
n = random.randint(1, 1000)

# Step 2: Initialize guess variable and counter
guess = -1
guesses = 0

# Step 3: Run the loop until the guess is correct
while guess != n:
    guess = int(input("Enter the number: "))
    guesses += 1

    if guess > n:
        print("Lower number please.")
    elif guess < n:
        print("Higher number please.")

# Step 4: When correct guess
print(f"🎉 You have guessed the number {n} correctly in {guesses} attempts!")
