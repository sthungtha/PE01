def count_word_frequency(text):
    # -------------------------------------------------
    # Step 1: Function receives the input text
    # -------------------------------------------------
    print("STEP 1: Function received the following text:")
    print(text)
    print("-" * 50)

    # -------------------------------------------------
    # Step 3: Conditional sentence (empty input check)
    # -------------------------------------------------
    if not text:
        print("STEP 3: Input is empty. Returning empty dictionary.")
        return {}
    print("STEP 3: Input is not empty. Proceeding with processing.")
    print("-" * 50)

    # -------------------------------------------------
    # Clean text (remove punctuation + lowercase)
    # -------------------------------------------------
    text = (
        text.lower()
            .replace(",", "")
            .replace(".", "")
            .replace("!", "")
            .replace("?", "")
            .replace("'", "")
    )
    print("Cleaned text (lowercase, no punctuation):")
    print(text)
    print("-" * 50)

    # -------------------------------------------------
    # Split into words
    # -------------------------------------------------
    words = text.split()
    print("Words extracted from text:")
    print(words)
    print("-" * 50)

    # -------------------------------------------------
    # Step 2: Create dictionary to store frequencies
    # -------------------------------------------------
    frequency = {}
    print("STEP 2: Empty dictionary created:")
    print(frequency)
    print("-" * 50)

    # -------------------------------------------------
    # Step 5: Recursive function to process words
    # -------------------------------------------------
    print("STEP 5: Starting recursive processing of words...")
    print("-" * 50)

    def process_words(words, index):
        if index == len(words):
            print("STEP 5: Recursion complete. All words processed.")
            print("-" * 50)
            return

        word = words[index]

        # Update dictionary
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

        # Print actual dictionary after each recursive update
        print(f"Processed '{word}'. Current dictionary:")
        print(frequency)

        process_words(words, index + 1)

    process_words(words, 0)

    return frequency


# -------------------------------------------------
# Test the Word Frequency Counter
# -------------------------------------------------
text = "This is a sample text. It contains some words. Some words are repeated, like 'is' and 'words'."
frequency_dict = count_word_frequency(text)

# -------------------------------------------------
# Step 4: Loop to print final results
# -------------------------------------------------
print("STEP 4: Looping through dictionary to print final frequencies:")
print("-" * 50)
for word, count in frequency_dict.items():
    print(f"{word}: {count}")
