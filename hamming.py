#Given two strings of equal length, return the number of characters that are different between the two strings.

def hamming (first_word, second_word):

	first_word_length = len(first_word)
	second_word_length = len(second_word)
	first = list(first_word)
	second = list(second_word)
	counter = 0
	
	
	if first_word_length != second_word_length: 
		print ("The first and second argument must be the same amount of characters, please try again")
		return
	else: 
		index = 0
		while index < len(first_word): 		
			if first[index] == second[index]:
				counter += 1
			index += 1
		return print(counter)

hamming ("adventure", "knowledge")


