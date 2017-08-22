def shopping():

	shopping_list = ["Milk", "Bread", "Bananas"]
	item = input("enter an item ")
	shopping_list.append(item)

	len_of_list = len(shopping_list)

	while len_of_list > 0:
		print(len_of_list)
		len_of_list -= 1
		for item in shopping_list:
			print(item)



shopping()