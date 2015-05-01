import random

def deck():
	cards = []
	signs = ["spades", "hearts", "clubs", "diamonds"]
	for i in range(1,15):
		for j in signs:
			cards.append((i,j))
	return cards												#get the deck of cards 
print deck()													#show me the cards

	random.shuffle(cards)
	for i in range(27):
		player1_hand = []
		cards.pop()
	player2_hand = cards
	return player1_hand, player2_hand



#def war(deck_one, deck_two):
#
#
#
#
#