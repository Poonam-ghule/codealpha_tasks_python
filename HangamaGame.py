import random

word = ['rose','lily','lotus','sunflower','bluebell','iris','basil']
word = random.choice(word)
guessed =  ['_'] * len(word)
incorrect_guessed_allowed = 6
incorrect_guessed = 0

print("Welcome to Hangaman!")
print("You have", incorrect_guessed_allowed, "chances to guess the word.")

while True:
    print(' '.join(guessed))

    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    
    else:
        incorrect_guessed += 1
        print("Incorrect guess. You have", incorrect_guessed_allowed - incorrect_guessed, "chance left.")


    if '_' not in guessed:
        print(' '.join(guessed))
        print("Congratulation, you won!")
        break

    if incorrect_guessed == incorrect_guessed_allowed:
        print("You lost. The word was", word)
        break