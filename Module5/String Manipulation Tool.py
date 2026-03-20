# String Manipulation Tool

# 1. Prompt the user to enter a string
text = input("Enter a string: ")

# 2. Display menu options
print("\nChoose an option:")
print("1. Convert to UPPERCASE")
print("2. Convert to lowercase")
print("3. Slice the string")
print("4. Get string length")
print("5. Display each character on a new line")

# 3. Get user choice
choice = input("\nEnter your choice (1-5): ")

# 4. Perform the selected operation
if choice == "1":
    print("\nUppercase:", text.upper())

elif choice == "2":
    print("\nLowercase:", text.lower())

elif choice == "3":
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    print("\nSliced string:", text[start:end])

elif choice == "4":
    print("\nLength of string:", len(text))

elif choice == "5":
    print("\nCharacters in the string:")
    for char in text:
        print(char)

else:
    print("\nInvalid choice. Please select a number from 1 to 5.")
