def isVowel():

	vowel_list = ["a", "e", "i", "o", "u"]

	user_letter = input()
	vowel = 0

	if user_letter in vowel_list:
		vowel = 1

	# for item in vowel_list:
	# 	if user_letter == item or user_letter == item.upper():
	# 		vowel = 1

	if vowel == 1:
		print("Letter is a vowel.")
	elif user_letter == "y" or user_letter == "Y":
		print("Letter is sometimes a vowel and sometimes a consonant.")
	else:
		print("Letter is a consonant.")

isVowel()