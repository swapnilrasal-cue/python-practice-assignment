import random

def draw_random_word():
	with open("sowpods.txt", 'r') as f:
		words = f.readlines()
	index = random.randint(0, len(words) - 1)
	word = words[index].strip()
	return word


def ask_user_for_guess_letter():
	letter = input("Guess your letter: ")
	return letter.strip().upper()


def generate_word_string(word, letters_guessed):
	guessed_list = []
	for letter in word:
		if letter in letters_guessed:
			guessed_list.append(letter.upper())
		else:
			guessed_list.append("_")
	return " ".join(guessed_list)


if __name__ == '__main__':
	WORD = draw_random_word()

	letters_to_guess = set(WORD)
	correct_letters_guessed = set()
	incorrect_letters_guessed = set()
	num_guesses = 0

	print("Welcome to Hangman!")
	while (len(letters_to_guess) > 0) and num_guesses < 6:
		guess = ask_user_for_guess_letter()

		if guess in correct_letters_guessed or \
				guess in incorrect_letters_guessed:
			print("You already guessed that letter.")
			continue

		if guess in letters_to_guess:
			letters_to_guess.remove(guess)
			correct_letters_guessed.add(guess)
		else:
			incorrect_letters_guessed.add(guess)
			num_guesses += 1

		word_string = generate_word_string(WORD, correct_letters_guessed)
		print(word_string)
		print("You have {} guesses left".format(6 - num_guesses))

	if num_guesses < 6:
		print("Congratulations! You correctly guessed the word {}".format(WORD))
	else:
		print("Sorry, you list! Your word was {}".format(WORD))