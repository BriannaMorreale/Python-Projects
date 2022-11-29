# Brianna Morreale
# 4/28/22
# Hangman Final Project

import random

file_name = "words.txt"

# Welcomes the user
def prompts():
	print("\nWelcome to Hangman!")
	print("To play you will have to guess a letter in a random word.")
	print("You will have 10 tries to guess.")

# Generates the random word
def random_word():
	# Reads the file in, randomly chooses a word
	with open(file_name) as f:
		lines = f.read()
		words = lines.split()
		keyword = random.choice(words)
		return keyword
	
# All of the game play		
def game(random_word):
	turns = 10
	hidden_word = "_ "*len(random_word)
	word_letters = list(random_word)
	used_letters =[]
	check_word = []
	
	# Used to see if the user has guessed every letter correct
	for r in random_word:
		check_word.append(r)
		check_word.append(" ")
		
	check_word.pop()
	check_word = "".join(check_word)


	prompts()
	print(f"\n {hidden_word} \n")
	
	# Won't go if they run out of turns	
	while turns > 0:
		used = True
		guess = str(input("Guess a letter/word:\n"))
		
		# If the user types a number
		if guess.isalpha() == False:
			print("Please use a letter in the alphabet.")
		
		try:
			# If they guess a single letter
			if len(guess) == 1:
				# If they already guessed the letter
				if guess in used_letters:
					print("This letter has already been used.")
					used = False
				if used == True:
					# If the letter is not in the word
					if guess not in random_word:
						turns -=1
						print(f"\n{guess} is not in the word.")
						print(f"{turns} attempts left.")
						# Adds it to a list 
						used_letters.append(guess)
					# If the letter is in the word
					if guess in random_word:
						turns -=1
						print(f"{turns} attempts left.")
						used_letters.append(guess)
						# Finds where the letter is/ letters are
						for i in range(len(random_word)):
							if guess == word_letters[i]:
								# Turns the underlines into a list
								h = hidden_word.replace(" ", "")
								temp = list(h)
								# Replaces the underline with letter
								temp[i] = guess
								# Formats it back to normal
								hidden_word = " ".join(temp)
						
						# If the user guesses every letter
						if hidden_word == check_word:
							print(f"{hidden_word} \n")
							print("\nCongrats! You guessed the word!")
							print(f"You did it in {turns} attempts.")
							print("You won!")
							play_again()
							break
								
			# If the user guesses a word		
			elif len(guess) != 1:
				if guess.lower() != random_word.lower():
					print("\nIncorect word. You lost.")
					print(f"The word was {random_word}.\n")
					play_again()
					break
					
				if guess.lower() == random_word.lower():
					print("\nCongrats! You won!")
					print(f"The word was {random_word}.\n")
					play_again()
					break
		
		# In case the user types something incorrect		
		except ValueError:
			print("Please only use a letter from the alphabet.")
		
		print(f"{hidden_word} \n")
	
	# If the user runs out of turns, the game ends	
	if turns == 0:
		print("Sorry, you lost. Your person has been hanged.")
		print(f"The word was {random_word}.")
		play_again()
				
	# Function to allow the user to play again		
def play_again():
		ans = input("\nPlay again? Type 'yes' or 'no':\n")
		if ans.lower() == 'no':
			print("Thanks for playing. Goodbye.")
		else:
			play()

# Will start the game when called
def play():
	game(random_word())
		

# Calling the play function
play()

# The game will start by welcoming the user and providing instructions
# on how to play. Then it will show underlines to represent each
# letter in the word. It will prompt the user to guess a letter or word.
# If they guess a letter and it is in the word, it will be added in.
# If they guess a letter and it's not in the word, a message will appear
# telling them it's not there and will show the attempts left.
# If they have already guessed the letter, the game will let them know 
# and it will not penalize them. If they try to guess a word and it's
# right, a message will appear telling them they won. If it is wrong,
# it will tell them that they lost and provide the word. If they
# cannot guess the letters after 10 tries, it will tell them they
# lost and what the word was. After the game is finished, it will ask
# if they want to play again. If so, the game will restart with a 
# different word. If not, it will end and say goodbye.
