def bottle_deposits():

	oneLiterRefund = .1*float(input("How many <= 1 liter bottles do you have? "))
	biggerThanOneLiterRefund = .25*float(input("How many > 1 liter bottles do you have? "))

	totalRefund = oneLiterRefund+biggerThanOneLiterRefund

	print("Total refund: ${0:.2f}".format(totalRefund))


bottle_deposits()