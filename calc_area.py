def calc_area():

	length = 0
	width = 0

	print("Enter the room length in feet:")
	length = float(input())
	print("Enter the room width in feet:")
	width = float(input())	

	print("The room area is: ", str(length*width), " square feet")
	
calc_area()