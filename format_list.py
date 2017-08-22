def format_list(list_of_things = []):
	
	list_with_commas = ""
	newList = list_of_things
	#newList = ['dog','cat','bird','horse','turtle']
	listLength = len(newList)-1
	
	if listLength > 0:
		x = 0

		while x < listLength:
			#print(newList)
			if(newList[x] != ',' and newList[x+1] != ','):
				newList.insert(x+1,",")
				newList.insert(x+2," ")
				listLength = len(newList)-1
				x += 3
			else:
				x += 1

		newList[len(newList)-3] = " and"

	for item in newList:
		list_with_commas = list_with_commas + str(item)

	#print(list_with_commas)

	return list_with_commas

#format_list()

if __name__ == '__main__':
	
	list_of_things = []
	item = input()

	while item != "":
		list_of_things.append(item)
		item = input()

	print(format_list(list_of_things))

