# -----------------------------------------
# User Profile Generator
# -----------------------------------------
# This script collects user information and
# demonstrates string manipulation techniques:
# 1. String concatenation
# 2. String formatting
# 3. Escape characters
# 4. String methods
# -----------------------------------------

# 1. Prompt the user to enter their details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
occupation = input("Enter your occupation: ")

# 2. STRING CONCATENATION:
# Combine first and last name into a full name
full_name = first_name + " " + last_name

# 3. STRING FORMATTING:
# Create a sentence including age, city, and occupation
profile_sentence = (
    f"You are {age} years old, living in {city}, "
    f"and working as a {occupation}."
)

# 4. ESCAPE CHARACTERS:
# \" adds quotation marks
# \n adds a new line
profile_description = (
    f"\"{full_name}\" is your full name.\n{profile_sentence}"
)

# 5. STRING METHODS:
# Convert full name to uppercase
full_name_upper = full_name.upper()

# If occupation starts with a vowel, replace "a" with "an"
# (as required by the project instructions)
if occupation.startswith(("a", "e", "i", "o", "u")):
    profile_description = profile_description.replace(" a ", " an ")

# -----------------------------------------
# Display the final profile
# -----------------------------------------
print("\n--- USER PROFILE ---")
print("Full Name:", full_name_upper)
print(profile_description)
print("Formatted Sentence:", profile_sentence)
print("-------------------")
