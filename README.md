#Description
The Random Password Generator is a simple Python project that generates a password using random digits. Users can enter the desired password length, and the program will generate a sequence of random numbers from 0 to 9. This project helps beginners understand user input, loops, and random number generation in Python.

#Features
>Generates a random numeric password.
>User chooses the password length.
>Uses the random module for number generation.
>Demonstrates the use of while loops and user input.

#Requirements
>Python 3.x
>Code
>Python
print("WELCOME TO PASSWORD GENERATOR")
print("You can generate random password")
 
l = int(input("Enter length of password: "))
 
i = 1
while i <= l:
   import random
   n = random.randint(0, 9)
   print(f"Digit({i})={n}")
   i += 1

#How to Run
Save the code as password_generator.py.
Open a terminal or command prompt.
Run the program:

#Shell
>python password_generator.py
>Enter the desired password length.
>The program will generate random digits as the password.

#Example Output
>Plain Text
WELCOME TO PASSWORD GENERATOR
You can generate random password
Enter length of password: 5
 
Digit(1)=7
Digit(2)=2
Digit(3)=9
Digit(4)=1
Digit(5)=4

#Learning Concepts
>Python input() function
>while loops
>Random number generation using random.randint()
>Variables and counters
>Basic program flow
>Future Improvements
>Generate passwords using letters and special characters.
>Combine generated digits into a single password string.
>Add password strength levels.
