def multiplication_table():

	print("\t".format(""), end="")
	for x in range(1,11):
		print(x, "\t".format(""), end="")
	print('\n')
	
	for x in range(1,11):
		print(x, "\t".format(""), end="")
		for y in range(1,11):
			print(x*y, "\t".format(""), end="")
		print('\n')

multiplication_table()