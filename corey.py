import random

def deck():													#Create cards for all suites
	cards = []
	signs = ["spades", "hearts", "clubs", "diamonds"]
	for i in range(1,15):
		for j in signs:
			cards.append((i,j))

	random.shuffle(cards)
	player1_hand = []
	for i in range(27):										#split deck for two players
		a = cards.pop()
		player1_hand.append(a)
	player2_hand = cards
	print player1_hand										#These worked, will need deleted
	print player2_hand

#deck()

player1_pile = []
player2_pile = []

def war(deck_one, deck_two):
	for i in range(1):
	
	
		if len(player1_hand) != 0 and len(player2_hand) != 0:			#if decks are not empty
			player1_card = player1_hand.pop()							
			player2_card = player2_hand.pop()
			if player1_card[0] != player2_card[0]:						#if the value of cards are not equal
				if player1_card[0] > player2_card[0]:					#if p1s is greater than p2s value
					player1_pile.append(player1_card)    				#p1 gets takes both cards
					player1_pile.append(player2_card)
				else:
					player2_pile.append(player1_card)					#if not, then p2 is > and gets both cards.
					player2_pile.append(player2_card)	
		
		
			else:														#if value of cards is equal
				
				
		else:															#if not more cards in either's deck
			player1_hand = player1_hand + player1_pile					#Then add your pile to your deck
			player2_hand = player2_hand + player2_pile
		
			#Need to shuffle at some point