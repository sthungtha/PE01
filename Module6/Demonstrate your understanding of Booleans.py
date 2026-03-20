print("Answer the following questions with yes or no.\n")

# 1. Ask the user about their preferences
action = input("Do you like action movies? ").lower() == "yes"
comedy = input("Do you enjoy comedies? ").lower() == "yes"
romance = input("Do you enjoy romance movies? ").lower() == "yes"

# 2. Combine booleans using logical operators
action_comedy = action and comedy and not romance
action_romance = action and romance and not comedy
comedy_romance = comedy and romance and not action

# 3. Determine single-genre fallback
if action_comedy:
    genre = "Action-Comedy"
elif action_romance:
    genre = "Action-Romance"
elif comedy_romance:
    genre = "Comedy-Romance"
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif romance:
    genre = "Romance"
else:
    genre = "Unknown"

# 4. Recommend movies using conditional statements

if genre == "Action-Comedy":
    print("You might enjoy: The Nice Guys, 21 Jump Street, Rush Hour")

elif genre == "Action-Romance":
    print("You might enjoy: Mr. & Mrs. Smith, The Mask of Zorro, True Lies")

elif genre == "Comedy-Romance":
    print("You might enjoy: Crazy Rich Asians, The Proposal, 10 Things I Hate About You")

elif genre == "Action":
    print("You might enjoy: John Wick, Mad Max: Fury Road, Gladiator")

elif genre == "Comedy":
    print("You might enjoy: Superbad, Step Brothers, The Hangover")

elif genre == "Romance":
    print("You might enjoy: La La Land, The Notebook, Pride & Prejudice")

else:
    print("It seems you’re not into these genres")
