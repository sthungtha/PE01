import random  # Importing the random module

# Creating a random integer between 1 and 100
random_number = random.randint(1, 100)   # snake_case
RandomNumber = random_number             # PascalCase
randomNumber = random_number             # camelCase

# Printing the random number and its data type
print("Random Number:", random_number)
print('Data Type:', type(random_number))

# Type conversions
float_number = float(random_number)
complex_number = complex(random_number)

print("As Float:", float_number)
print("Float Type:", type(float_number))

print("As Complex:", complex_number)
print('Complex Type:', type(complex_number))
