# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
#print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Enter a letter from A-Z: ').lower()

    if letter in ["a", "e", "i", "o", "u"]:
            print(f'The letter {letter} is a vowel.')
    elif letter in ["b", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            print(f'The letter {letter} is a consonant.')
    else:
        print('Invalid input.') 
     
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = int(input('Please input your age: '))

    if age <= 0:
        print(f'You cannot be under the age of zero. Please input a valid age.')
    elif age >= 18:
        print(f'You are eligibile to vote!')
    elif age <= 17:
        print(f'You are not eligible to vote until you turn 18.')

# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    age = int(input('Please input the age of your dog: '))

    if age <= 2:
        print(f'Your dog is {age*10} in dog years.')
    elif age >= 3:
        print(f'Your dog is {(age-2)*7+20} in dog years.')
# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold= input('Is it cold? (Enter yes/no): ').lower()
    raining= input ('Is it raining? (Enter yes/no): ').lower()

    if(cold=="yes" and raining=="yes"):
        print(f'Wear a waterproof coat.')
    elif(cold=="yes" and raining=="no"):
        print(f'Wear a warm coat.')
    elif(cold=="no" and raining=="yes"):
        print(f'Carry an umbrella.')
    elif(cold=="no" and raining=="no"):
        print(f'Wear light clothing.')
# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month= input('Enter the first three letters of the month: ').lower()
    day= int(input('Enter the day of the month: '))

    if day <= 0 or day >= 32:
        print(f'Invalid input. Enter a number between 1-31.')
        return
    if day >= 31 and month in ["apr", "jun", "sep", "nov"]:
        print(f'Invalid input. Enter a number between 1-30.')
        return
    if  day >= 30 and month == "feb":
        print(f'Invalid input. Enter a number between 1-29.')
        return
    if month not in  ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]:
        print(f'Invalid input. Enter the first three letters of the month such as "Jan."')
        return
    if month in ["jan", "feb"] or (month == "dec" and day >= 21) or (month == "mar" and day <= 19):
        print(f'{month} {day} is in winter.')
    elif month in ["apr", "may"] or (month == "jun" and day <= 20) or (month == "mar" and day >= 20):
        print(f'{month} {day} is in spring.')
    elif month in ["jul", "aug"] or (month == "sep" and day <= 21) or (month == "jun" and day >= 21):
        print(f'{month} {day} is in summer.')
    elif month in ["oct", "nov"] or (month == "dec" and day <= 20) or (month == "sep" and day >= 22):
        print(f'{month} {day} is in fall.')
# Call the function
determine_season()
