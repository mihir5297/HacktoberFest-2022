import random
from hangman_art import logo, stages
from hangman_words import word_list
print(logo)
#  choose a word randomly from list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# it will randomly choose the word from the list
# ask input from user and make it lower case.
# create an empty list and display and add as many dashes to it as the number of letters are tghere in chosen word
display = []
print(f'chosen word is = {chosen_word}')
for letter in range(word_length): #alternatively we can use the range function
    display += "_"
print(display)
#  guessing a letter for the chosen word
end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(stages[lives])
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    print(display)
    if "_" not in display:
        end_of_game = True
        print("YOU WIN")
    elif lives == 0:
        end_of_game = True
        print(stages[0])
        print("YOU LOSE")

