import random
from hangman_words import word_list
from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

game_over = False
lives = 6



while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"Sorry you already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"Sorry, {guess} is not in the word")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        game_over = True
        print("You Win.")
    from hangman_art import stages
    print(stages[lives])







