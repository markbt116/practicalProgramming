def triangle_type():

	first_Length = int(input("Enter first triangle length: "))
	second_Length = int(input("Enter second triangle length: "))
	third_Length = int(input("Enter third triangle length: "))

	# lengths = [int(input("Enter first triangle length: ")), int(input("Enter second triangle length: ")), int(input("Enter third triangle length: "))]

	#x,y = 0,0
	# totalEqualSides = 0
	# hasAnEqualSide = 0

	# while( x < len(lengths)-1):
	# 	y = x
	# 	while (y < len(lengths)-1):
	# 		if lengths[x] == lengths[y+1]:
	# 			totalEqualSides += 1
	# 			hasAnEqualSide = 1
	# 		y += 1
	# 	x += 1

	# if hasAnEqualSide > 0:
	# 	totalEqualSides += 1

	# print("Total equal sides: " + str(totalEqualSides))
	
	if first_Length == second_Length:
		if second_Length == third_Length:
			totalEqualSides = 3
		else:
			totalEqualSides = 2
	elif first_Length == third_Length:
		totalEqualSides = 2
	elif second_Length == third_Length:
		totalEqualSides = 2
	else:
		totalEqualSides = 0

	if totalEqualSides == 0:
		triangle = "scalene"
	elif totalEqualSides == 2:
		triangle = "isoceles"
	elif totalEqualSides == 3:
		triangle = "equilateral"

	print(triangle)
		


triangle_type()