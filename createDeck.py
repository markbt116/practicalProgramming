def createDeck():

	value = [2,3,4,5,6,7,8,9,'T','J','Q','K','A']
	suit = ['s','c','d','h']

	deck = []

	for n in suit:
		for i in value:
			card = (i,n)
			deck.append(card)

	return deck

createDeck()