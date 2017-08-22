def random_lottery_numbers():

	import random
	random.seed(a=None)

	lotteryTicket = []

	while len(lotteryTicket) < 6:
		randomNumber = random.randint(1,49)

		if randomNumber not in lotteryTicket:
			lotteryTicket.append(randomNumber)

	print(lotteryTicket)

	for x in range(0, len(lotteryTicket)):
		for n in range(0, (len(lotteryTicket)-1)):
			if lotteryTicket[n] > lotteryTicket[n+1]:
				lotteryTicket[n], lotteryTicket[n+1] = lotteryTicket[n+1], lotteryTicket[n] 
		print(lotteryTicket)

	print(lotteryTicket)

random_lottery_numbers()