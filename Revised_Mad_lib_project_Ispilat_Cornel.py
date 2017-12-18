# Global Variables

blanks = ["VERB", "NOUN1", "OCCUPATION", "NOUN2"]

easy_paragraph = '''John VERB in the NOUN1 most of the evenings, as he is a OCCUPATION, and knows the importance of his NOUN2, he likes to have a good fit.'''
medium_paragraph = '''John VERB at NOUN1 most of the mornings, being a OCCUPATION, he knows the importance of the NOUN2, also he likes to have a good fit.'''
hard_paragraph = '''John is VERB hard, at the local NOUN1, he is also known as a very good personal OCCUPATION, he has a perfect NOUN2 fit.'''

easy_answers = ["run", "park", "doctor", "health"]
medium_answers = ["eat", "home", "nutritionist", "breakfast"]
hard_answers = ["pushing", "gym", "trainer", "body"]

# Helper Functions

def greeting(player_name):
	print "\nGreat! Welcome, " + player_name + " ! This game is about to fill in the blanks for all the sentences provided. Now, please pick a level by entering in the appropriate number: "

# To display initial player and game information.
# Inputs: Inputted name of player.
# Outputs: Introduction to game greeting.

def get_setup(level):

# To group all the paragraphs and answers together.
# Inputs: Current level.
# Outputs: The specific paragraph and its answers associated with that level.

	if level == "1":
		print "\nYou chose level 1 - Easy.\n"
		return easy_paragraph, easy_answers

	elif level == "2":
		print "\nYou chose level 2 - Medium.\n"
		return medium_paragraph, medium_answers

	else:
		print "\nYou chose level 3 - Hard.\n"
		return hard_paragraph, hard_answers


def word_in_blanks(word, blanks):

# To single out every blank.
# Inputs: 'word' is the each blank in the 'blanks' list. 'blanks' is the list.
# Outputs: Returns 'word' if that matches up with the current word in the paragraph.

	for blank in blanks:  # For every blank in the blanks array.
		if blank in word:  # If blank is in answer.
			return blank
	return None
	

def replace_the_blank(word, replaced, blanks, user_answer, index):

# To replace each blank with its correct answer. Part 2.
# Inputs: 'blanks' list, the replaced paragraph that has the correct answers so far, if applicable,
# the 'user_answer' for that blank, the index number of that 'user_answer' to correctly match that with the right blank to fill in.
# Outputs: The correctly replaced paragraph.

	if word_in_blanks(word, blanks) == None:
			replaced.append(word)
	else:
		replacement = word_in_blanks(word, blanks)
		word = word.replace(replacement, user_answer.upper())

		if replacement == blanks[index]:
			if replacement not in replaced:
				replaced.append(word)
			else:
				position = replaced.index(replacement)
				replaced[position] = word

		else:
			replaced.append(replacement)
	return replaced

def fill_in_answers(paragraph, blanks, replaced, user_answer, index):

# To replace each blank with its correct answer.
# Inputs: Paragraph from level, 'blanks' list, the replaced paragraph that has the correct answers so far, if applicable,
# the 'user_answer' for that blank, the index number of that 'user_answer' to correctly match that with the right blank to fill in.
# Outputs: The correctly replaced paragraph.

	split_paragraph = paragraph.split()
	if type(replaced) == str:
		replaced = replaced.split()

	for word in split_paragraph:
		replace_the_blank(word, replaced, blanks, user_answer, index)

	replaced = " ".join(replaced)
	head, sep, tail = replaced.partition("fit.")  # To get rid of the extra 'replacements' that tacked on to the end of every paragraph. Inputs: The replaced paragraph.  Outputs: Cleaned replaced paragraph
	replaced = head + sep 
	return replaced

def collect_answers(level, paragraph, answers):

# To collect the user's answers.
# Inputs: The current level, its paragraph, and its answers.
# Outputs: The updated replaced paragraph, the index of each answer.

	replaced = []
	user_answer = ""

	index = 0
	for blank in blanks:

# Where the questions and answers gets stated.

		question = "\nWhat is your answer for " + blank + "?"
		print question
		user_answer = raw_input("Type here: ")
		user_answer = user_answer.lower()

		while user_answer != answers[index]:
			print "\nYour answer was wrong. Please try again.\n"
			user_answer = raw_input("Type it here again: ")
			user_answer = user_answer.lower()

		print "\nAwesome, that's correct!\n"
		replaced = fill_in_answers(paragraph, blanks, replaced, user_answer, index)
		print replaced

		index += 1

	return replaced, index

# Starting to play the 'game'.

def play_game():

# To execute the main program/game.
# Inputs: None.
# Outputs: Whole program.

	player_name = raw_input("What is the name of the current player? ")
	greeting(player_name)

	levels = ["easy", "medium", "hard"]
	for level in levels:
              
          level = raw_input("\nEasy - 1 | Medium - 2 | Hard - 3 |\n ")
          if level == "1" or level == "2" or level == "3":
              paragraph, answers = get_setup(level)
              print paragraph 
    
              replaced = collect_answers(level, paragraph, answers)
    
              print "\nYAY, " + player_name + ", YOU WON THE GAME!\n" 
    
        else:
            print "\nWRONG! Please pick an actual level, " + player_name + ". Game will now restart.\n"
        play_game()

play_game()
