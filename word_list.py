def word_list():

	listOfWords = []
	userWord = input()

	while (userWord != "quit" and userWord != ""):
		if userWord not in listOfWords:
			listOfWords.append(userWord)
		userWord = input()

	print(listOfWords)

word_list()