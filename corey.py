import random

def deck():													#Create cards for all suites
	cards = []
	signs = ["spades", "hearts", "clubs", "diamonds"]
	for i in range(1,14):
		for j in signs:
			cards.append((i,j))

	random.shuffle(cards)
	player1_hand = []
	for i in range(26):										#split deck for two players
		a = cards.pop()
		player1_hand.append(a)
	player2_hand = cards
	return player1_hand, player2_hand

pot = [] 
def war(deck_one, deck_two, player1_card, player2_card, player1_pile, player2_pile):
	global pot
	if len(deck_two) < 4:								#If players do not have enough cards to war..
		player1_pile += pot							#Then other player wins the war
		player1_pile.append(player1_card)
		player1_pile.append(player2_card)
		player1_pile += deck_two
		pot = []
	if len(deck_one) < 4:
		player2_pile += pot
		player2_pile.append(player1_card)			
		player2_pile.append(player2_card)
		player2_pile += deck_one
		pot = []
	else:													#If they do draw 3 face down, draw 1 to play with
		for i in range(3):
			a = deck_one.pop()
			pot.append(a)
			b = deck_two.pop()
			pot.append(b)
	
		new_player1_card = deck_one.pop()
		new_player2_card = deck_two.pop()
		pot.append(new_player1_card)
		pot.append(new_player2_card)
	
		if new_player1_card[0] == new_player2_card[0]:				#If tied again, do war a second time
			war(deck_one, deck_two, player1_card, player2_card, player1_pile, player2_pile)
		else:
			if new_player1_card[0] > new_player2_card[0]:
				player1_pile += pot
				player1_pile.append(player1_card)
				player1_pile.append(player2_card)
				pot = []
			else: 
				player2_pile += pot
				player2_pile.append(player1_card)			
				player2_pile.append(player2_card)
				pot = []

player1_pile = []	
player2_pile = []
deck_one , deck_two = deck()											#Uses the tuple from game to make two playing decks
def game(deck_one, deck_two):
	global player1_pile	
	global player2_pile
	for i in range(2):													#2 turns of one game
		while len(deck_one) != 0 and len(deck_two) != 0:		#if decks are not empty
			player1_card = deck_one.pop()							
			player2_card = deck_two.pop()
			if player1_card[0] != player2_card[0]:						#if the value of cards are not equal
				if player1_card[0] > player2_card[0]:					#if p1s is greater than p2s value
					player1_pile.append(player1_card)    				#p1 gets takes both cards
					player1_pile.append(player2_card)
				else:
					player2_pile.append(player1_card)					#if not, then p2 is > and gets both cards.
					player2_pile.append(player2_card)	
		
		
			else:														#if value of cards is equal
				war(deck_one, deck_two, player1_card, player2_card, player1_pile, player2_pile)		#War it out
				
		else:															#if not more cards in either's deck
			deck_one = deck_one + player1_pile					#Then add your pile to your deck
			deck_two = deck_two + player2_pile
			random.shuffle(deck_one)								#Shuffle cards
			random.shuffle(deck_two)
			player1_pile = []
			player2_pile = []
		print len(deck_one)
		print len(deck_two)
				
game(deck_one, deck_two)		
#Need to get player1 hand and player2 hand into this function


#window = pyglet.window.Window()