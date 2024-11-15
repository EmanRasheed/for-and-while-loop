#FA24-BBD-025
#Eman Rasheed
#Lab Assignment
#FOR LOOPS
#List Iteration
favorite_movies = [
    "The Shawshank Redemption",
    "The Dark Knight",
    "Inception",
    "Forrest Gump",
    "The Godfather",
    "Pulp Fiction",
    "The Matrix"
]
for movie in favorite_movies:
    print(movie)
for index, movie in enumerate(favorite_movies):
    print(f"Index {index}: {movie}")

#String Iteration
# Step 1: Create a string variable containing your full name
full_name = "John Doe"

# Step 2: Iterate over the string and print each character on a new line
for char in full_name:
    print(char)

# Step 3: Count the number of vowels in the string
vowels = "aeiouAEIOU"  # Define vowels (including uppercase)
vowel_count = 0

# Iterate over the string and count the vowels
for char in full_name:
    if char in vowels:
        vowel_count += 1

# Print the result
print(f"Number of vowels in the name: {vowel_count}")

#Dictionary Iteration
# Step 1: Create a dictionary with student names and their grades
students_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eva": 88
}

# Step 2: Iterate over the dictionary and print the name and grade of each student
for student, grade in students_grades.items():
    print(f"Student: {student}, Grade: {grade}")

# Step 3: Find the student with the highest grade
highest_grade_student = max(students_grades, key=students_grades.get)
highest_grade = students_grades[highest_grade_student]

# Print the student with the highest grade
print(f"The student with the highest grade is {highest_grade_student} with a grade of {highest_grade}.")

#Nested For Loops
# Step 1: Create a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Step 2: Iterate over the matrix and print each element
for row in matrix:
    for element in row:
        print(element, end=" ")  # Print each element in the same row on the same line
    print()  # Move to the next line after each row

# Step 3: Calculate the sum of all elements in the matrix
total_sum = sum(sum(row) for row in matrix)

# Print the sum of all elements
print(f"Sum of all elements in the matrix: {total_sum}")

#List Comprehension
 Using list comprehension to create a list of squares from 1 to 10
squares_comprehension = [number ** 2 for number in range(1, 11)]

# Print the list of squares
print("Squares using list comprehension:", squares_comprehension)

#WHILE LOOPS
#Counting with while loop
# Initialize the counter
counter = 1

# Use a while loop to count from 1 to 10
while counter <= 10:
    print(counter)
    counter += 1  # Increment the counter by 1
#Even Numbers
# Initialize the counter
number = 2

# Use a while loop to print even numbers from 1 to 20
while number <= 20:
    print(number)
    number += 2  # Increment the counter by 2 to get the next even number
#Sum Of Natural Numbers
# Initialize variables
sum_of_numbers = 0
counter = 1

# Using a while loop to sum the first 10 natural numbers
while counter <= 10:
    sum_of_numbers += counter
    counter += 1

# Print the result
print("The sum of the first 10 natural numbers is:", sum_of_numbers)
#USer Input With Condition
# Initialize the total sum to 0
total_sum = 0

# Loop to keep asking for numbers
while True:
    # Prompt the user to enter a number
    number = float(input("Enter a number (or a negative number to stop): "))
    
    # Check if the entered number is negative
    if number < 0:
        break  # Exit the loop if the number is negative
    
    # Add the positive number to the total sum
    total_sum += number

# Print the total sum
print("The total sum of the numbers entered is:", total_sum)
#Number Guessing Game
# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Start the guessing game
print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

while True:
    # Prompt the user for a guess
    guess = int(input("Enter your guess: "))
    
    # Increment the number of attempts
    attempts += 1
    
    # Check if the guess is correct
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number {target_number} in {attempts} attempts.")
        break  # Exit the loop when the user guesses correctly
#Factorial calculation
# Prompt the user to enter a positive integer
number = int(input("Enter a positive integer: "))

# Check if the input is a valid positive integer
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Initialize variables
    factorial = 1
    counter = 1
    
    # Using a while loop to calculate the factorial
    while counter <= number:
        factorial *= counter
        counter += 1
    
    # Print the result
    print(f"The factorial of {number} is: {factorial}")
#Average Calculator
# Initialize variables for sum and count
total_sum = 0
count = 0

# Start the loop
while True:
    # Prompt the user for input
    user_input = input("Enter a number (or 'done' to finish): ")
    
    # Check if the user wants to stop the loop
    if user_input.lower() == "done":
        break
    
    # Try to convert the input to a number
    try:
        number = float(user_input)
        total_sum += number  # Add the number to the total sum
        count += 1  # Increment the count of numbers entered
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# After the loop ends, calculate and print the average
if count > 0:
    average = total_sum / count
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers were entered.")
#Fibonacci Sequence
# Get the number n from the user
n = int(input("Enter a number n to print Fibonacci sequence up to: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the Fibonacci sequence up to n
print("Fibonacci sequence up to", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b  # Update a and b to the next two Fibonacci numbers




