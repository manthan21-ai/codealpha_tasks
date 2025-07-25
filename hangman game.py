import random

# List of 5 predefined words
word_list = ["white", "blue", "green", "orange", "red"]
# Randomly choose a word from the list
word_to_guess = random.choice(word_list)
guessed_letters = []
attempts_left = 6

# Create a hidden version of the word using underscores
hidden_word = ["_"] * len(word_to_guess)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while attempts_left > 0 and "_" in hidden_word:
    print("Word: ", " ".join(hidden_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                hidden_word[i] = guess
    else:
        print("Wrong guess.\n")
        attempts_left -= 1

# Game over logic
if "_" not in hidden_word:
    print(f"Congratulations! You guessed the word: {word_to_guess}")
else:
    print(f"Game over! The correct word was: {word_to_guess}")
