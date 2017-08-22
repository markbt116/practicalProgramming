def shuffle(deck = []):

	import random
	random.seed(a=None)

	for i in range(0,len(deck)-1):
		randomCardIndex = random.randint(0,51)
		deck[i], deck[randomCardIndex] = deck[randomCardIndex], deck[i]

shuffle()