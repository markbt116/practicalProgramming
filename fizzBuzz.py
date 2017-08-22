def fizzBuzz():

	for x in range(1,100):
		if(x%3==0):
			if(x%5==0):
				print("FizzBuzz")
			else:
				print("Fizz")
		elif(x%5==0):
			print("Buzz")
		else:
			print(x)


	# for x in range(1,100):
	# 	if(x%3==0):
	# 		print("Fizz",end="")
	# 	if(x%5==0):
	# 		print("Buzz",end='\n')
	# 	elif(x%3!=0):
	# 		print('\n',x,end='\n')

fizzBuzz()