"""
This program is a random password generator. It will first ask the user how many characters it wants to generate and whether or not it should contain special (and allowed) characters.

The program will keep looping until the user forcefully exits (ctrl c) because they found a suitable password.

Note: This is (currently) a terminal-only output and may not be the safest method to generate a password.

"""

import sys, time, random

# The main function that will generate the random password
def generator(length, haveSpecial):
    options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if haveSpecial: # If True, the program can generate more complicated passwords
        options.extend(["#", "$", "%", "&", "*", "?", "_", "-", "."])

    password = ""

    for i in range(length): # Loop based on the length of password given by the user
        password += random.choice(options)

    return password

while True: # Valid user input loop
    try: # Checks if the user enters a number or not (letter, nothing, etc.)
        charPass = int(input("How many characters do you want the password to have? Enter the number.\n"))
    except ValueError:
        print("Please enter a number.")
        continue

    containSpecial = input("Do you want the passwords to have special characters (e.g. _)? 1 if yes, 0 if no.\n")
    if containSpecial == "1":
        containSpecial = True
    elif containSpecial == "0":
        containSpecial = False
    else:
        print("Since you entered none of the choices, we will automatically add special characters.")
        containSpecial = True

    break

while True: # Generating the passwords loop
    try:
        print("Generated Password: " + generator(charPass, containSpecial))
        time.sleep(1.25) # To ensure that the program won't spam and eventually crash
    except:
        print("\nThank you for using this program!")
        sys.exit()

