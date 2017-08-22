def createDeck():

	value = [2,3,4,5,6,7,8,9,'T','J','Q','K','A']
	suit = ['s','c','d','h']

	deck = []

	for n in suit:
		for i in value:
			card = (i,n)
			deck.append(card)

	print(deck,'\n'*2)

	return deck


def shuffle(deck = []):

	import random
	random.seed(a=None)

	for i in range(0,len(deck)-1):
		randomIndex1 = random.randint(0,51)
		randomIndex2 = random.randint(0,51)
		deck[randomIndex2], deck[randomIndex1] = deck[randomIndex1], deck[randomIndex2]

	return deck


if __name__ == '__main__':
	
	#print(createDeck(),'\n'*2)
	deck = shuffle(createDeck())
	print(deck)

	#main()
