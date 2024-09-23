import random

print("Welcome to the Word Guessing Game! :D")
#display rules for users
print('''Rules:
1. Choose a category to play.
2. Guess the word based on the hints provided.
3. You have a limited number of attempts.
Finally, thanks for playing this game made with ❤️ by Aavash.''')

print()

# Categories
categories = {
    "1": ["Cat", "Dog", "Tiger", "Lion", "Peacock", "Camel", "Pigeon"],
    "2": ["Supra", "Porsche", "Lamborghini", "Ford", "Mercedes", "Audi", "Mustang"],
    "3": ["Nepal", "Malaysia", "Qatar", "Dubai", "America", "China", "India"]
}
#choose one catagory
print("Choose a category: ")
print("1. Animals")
print("2. Cars")
print("3. Countries")
choose = input("Enter 1, 2, or 3: ")

if choose in categories:
    words = categories[choose]
    selected_word = random.choice(words).lower()
    attempts = 5 #this is total attempts.
    guessed_letters = []

    print(f"\nYou've chosen: {selected_word}")
    print("Guess the word! You have 5 attempts.")

    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in selected_word])
        print(f"\nCurrent word: {display_word}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in selected_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in selected_word):
            print(f"\nCongratulations! You've guessed the word: {selected_word}")
            break
    else:
        print(f"\nSorry, you've run out of max guesses! the word was: {selected_word}")

else:
    print("Invalid Input :/ ")
