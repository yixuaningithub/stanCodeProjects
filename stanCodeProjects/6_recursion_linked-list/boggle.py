"""
File: boggle.py
Name: Yi-Syuan Chung
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	name_list = read_dictionary(FILE)								# dict to store name and separate the prefix
	row = 1															# input four rows of letters
	row_letter = []													# list to store input letters
	while row <= 4:
		letter = input(str(row)+" row of letters: ")				# letters of a row
		letter.split()
		if len(letter.split()) != 4:
			print("Illegal Input")
			continue
		for ch in letter.split():
			if len(ch) > 1:
				print("Illegal Input")
				break
		row_letter.append(letter.lower().split())
		row += 1
	# row_letter = [["f", "y", "c", "l"], ["i", "o", "m", "g"], ["o", "r", "i", "l"], ["h", "j", "h", "u"]]
	find_words(row_letter, name_list)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(file):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	name_list = {}
	with open(file, "r") as f:
		for line in f:
			if len(line) >= 5:											# only store the words more than 4 letters
				if line[0] in name_list:								# if it exists the prefix
					name_list[line[0]].append(line[:-1])
				else:
					name_list[line[0]] = [line[:-1]]					# add the prefix into key, name into value
	return name_list


def has_prefix(sub_s, name_list, ans_word):
	"""
	:param ans_word: (list) The word satisfies the request
	:param name_list: (dict) the dict stores prefix and the total names
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if sub_s[0] in name_list:
		for name in name_list[sub_s[0]]:
			if name.startswith(sub_s):									# if the name starts with sub_s
				if sub_s == name and sub_s not in ans_word:				# check if the sub_s == name and not exist in the ans_word yet
					print("Found \""+sub_s+"\"")
					ans_word.append(sub_s)
				return True
	return False


def find_words(row_letter, name_list):
	ans_word = []														# list to store ans
	for i in range(4):
		for j in range(4):
			find_words_helper(row_letter, i, j, name_list, "", ans_word, up=True, down=True, left=True, right=True,
																					lu=True, ld=True, ru=True, rd=True)
	print("There are "+str(len(ans_word))+" words in total.")


def find_words_helper(row_letter, i, j, name_list, word, ans_word, up, down, left, right, lu, ld, ru, rd):
	if len(word) == 0:
		word += row_letter[i][j]
	if i > 0 and up:												# if i-1 >= 0 and it didn't go down on the last step
		word += row_letter[i-1][j]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i-1, j, name_list, word, ans_word, up=True, down=False, left=True, right=True,
																					lu=True, ld=True, ru=True, rd=True)
		word = word[:-1]
	if i < 3 and down:												# if i+1 <= 0 and it didn't go up on the last step
		word += row_letter[i+1][j]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i+1, j, name_list, word, ans_word, up=False, down=True, left=True, right=True,
																					lu=True, ld=True, ru=True, rd=True)
		word = word[:-1]
	if j > 0 and left:												# if j-1 >= 0 and it didn't go right on the last step
		word += row_letter[i][j-1]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i, j-1, name_list, word, ans_word, up=True, down=True, left=True, right=False,
																					lu=True, ld=True, ru=True, rd=True)
		word = word[:-1]
	if j < 3 and right:												# if j+1 <= 3 and it didn't go left on the last step
		word += row_letter[i][j+1]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i, j+1, name_list, word, ans_word, up=True, down=True, left=False, right=True,
																					lu=True, ld=True, ru=True, rd=True)
		word = word[:-1]
	if i > 0 and j > 0 and lu:						# if i-1 >= 0, j-1 >= 0 and it didn't go right down on the last step
		word += row_letter[i-1][j-1]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i-1, j-1, name_list, word, ans_word, up=True, down=True, left=True, right=True,
																					lu=True, ld=True, ru=True, rd=False)
		word = word[:-1]
	if i > 0 and j < 3 and ru:						# if i-1 >= 0, j+1 <= 3 and it didn't go left down on the last step
		word += row_letter[i-1][j+1]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i-1, j+1, name_list, word, ans_word, up=True, down=True, left=True, right=True,
																					lu=True, ld=False, ru=True, rd=True)
		word = word[:-1]
	if i < 3 and j > 0 and ld:						# if i+1 <= 3, j-1 >= 0 and it didn't go right up on the last step
		word += row_letter[i+1][j-1]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i+1, j-1, name_list, word, ans_word, up=True, down=True, left=True,right=True,
																					lu=True, ld=True, ru=False, rd=True)
		word = word[:-1]
	if i < 3 and j < 3 and rd:						# if i+1 <= 3, j+1 <= 3 and it didn't go left up on the last step
		word += row_letter[i+1][j+1]
		if has_prefix(word, name_list, ans_word):
			find_words_helper(row_letter, i+1, j+1, name_list, word, ans_word, up=True, down=True, left=True, right=True,
																					lu=False, ld=True, ru=True, rd=True)
		word = word[:-1]


if __name__ == '__main__':
	main()
