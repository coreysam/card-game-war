import random
import pyglet

window = pyglet.window.Window()

def deck():									#Create cards for all suites
"""
Invocation: List of deck of cards
Meaning: This function is for creating the deck of cards used in the game. 
Each sign is assigned a number 2-15, with two being the two card and 15 being an ace. It
then adds these cards to deck to be used for the game. These cards are stored in a tuple 
and then shuffled. Then 26 cards are dealt to player1 and player2.
Preconditions: The list is originally empty.
Postconditions: The returned value is a list of two lists containing tuples of a value and sign of a card.
"""	
	cards = []
	signs = ["spades", "hearts", "clubs", "diamonds"]
	for i in range(2,15):								#Loops through and adds a value to the 4 suites	
		for j in signs:
			cards.append((i,j))

	random.shuffle(cards)
	player1_hand = []
	for i in range(26):								#split deck for two players
		a = cards.pop()
		player1_hand.append(a)
	player2_hand = cards
	return player1_hand, player2_hand
	
imageWidth = 100
imageHeight = 100

pot = [] 
def war(deck_one, deck_two, player1_card, player2_card, player1_pile, player2_pile):
"""
Invocation: War
Meaning: This function creates what to do in the case that the two players play the same value cards.
Each player lays down 3 face down cards and 1 card face up. Who ever has the greatest card
wins all the cards laid out. If the players cards tie again, it runs through the function again.
Preconditions: deck_one and deck_two should be a list of tuples. player1_card and player2_card are both tuples with the first element being equal. player1_pile and player2_pile is also a list of tuples.
Postconditions: This function compares two other tuples and compares the first elements and sends the higher numbered element to the players pile list.
"""
	global pot
	global image3
	global image4
	global image5
	global image6
	global image7
	global image8
	global image9
	global image10	
	if len(deck_two) < 4:								#If players do not have enough cards to war..
		if len(pot) == 0:							#If pot is empty..used at first to make sure to add correctly
			player1_pile.append(player1_card)
			player1_pile.append(player2_card)
			player1_pile += deck_two
		else:
			player1_pile += pot						#If cards in pot, then other player wins the war and gets cards
			player1_pile.append(player1_card)
			player1_pile.append(player2_card)
			player1_pile += deck_two
			pot = []
	elif len(deck_one) < 4:
		if len(pot) == 0:
			player2_pile.append(player1_card)			
			player2_pile.append(player2_card)
			player2_pile += deck_one
		else:
			player2_pile += pot
			player2_pile.append(player1_card)			
			player2_pile.append(player2_card)
			player2_pile += deck_one
			pot = []
	else:											#If they do draw 3 face down, draw 1 to play with
		for i in range(3):
			a = deck_one.pop()
			pot.append(a)
			b = deck_two.pop()
			pot.append(b)
	
		new_player1_card = deck_one.pop()
		new_player2_card = deck_two.pop()
		str3 = str(new_player1_card[0]) + '_of_' + str(new_player1_card[1]) + '.png'
		str4 = str(new_player2_card[0]) + '_of_' + str(new_player2_card[1]) + '.png'			#images being added
		image3 = pyglet.resource.image('cards/' + str3)
		image4 = pyglet.resource.image('cards/' + str4)
		image3.width = imageWidth
		image3.height = imageHeight
		image4.width = imageWidth
		image4.height = imageHeight
		image5 = pyglet.resource.image('cards/penguin.png')
		image6 = pyglet.resource.image('cards/penguin.png')
		image7 = pyglet.resource.image('cards/penguin.png')
		image8 = pyglet.resource.image('cards/penguin.png')
		image9 = pyglet.resource.image('cards/penguin.png')
		image10 = pyglet.resource.image('cards/penguin.png')
		image5.width = imageWidth
		image5.height = imageHeight
		image6.width = imageWidth
		image6.height = imageHeight
		image7.width = imageWidth
		image7.height = imageHeight
		image8.width = imageWidth
		image8.height = imageHeight
		image9.width = imageWidth
		image9.height = imageHeight
		image10.width = imageWidth
		image10.height = imageHeight
		
		pot.append(new_player1_card)
		pot.append(new_player2_card)
	
		if new_player1_card[0] == new_player2_card[0]:		#If tied again, do war a second time
			war(deck_one, deck_two, player1_card, player2_card, player1_pile, player2_pile)			#If tied again, do war a second time
		else:
			if new_player1_card[0] > new_player2_card[0]:
				player1_pile += pot									#comparing new cards
				player1_pile.append(player1_card)
				player1_pile.append(player2_card)
				pot = []
			else: 
				player2_pile += pot
				player2_pile.append(player1_card)			
				player2_pile.append(player2_card)
				pot = []
				
image1 = pyglet.resource.image('cards/penguin.png')
image2 = pyglet.resource.image('cards/penguin.png')
image3 = pyglet.resource.image('cards/14_of_clubs.png')
image4 = pyglet.resource.image('cards/14_of_diamonds.png')
player1_pile = []	
player2_pile = []
player1_card = (2, 'spades')
player2_card = (3, 'hearts')
deck_one , deck_two = deck()	
label = pyglet.text.Label(' ')								

def play_one_turn(deck_one, deck_two):
"""
Invocation: one_turn(deck_one, deck_two)
Meaning: This function takes player1 and player2 through 1 turn and using pyglet to show the card on the window.
cards.
Preconditions:deck_one and deck_two should be a list of tuples.
Postconditions: The returned value is to place tuples in a players pile list.
"""
	global player1_pile	
	global player2_pile
	global image1
	global image2
	global image3
	global image4
	global player1_card
	global player2_card	
	global label									
	if len(deck_one) != 0 and len(deck_two) != 0:		#if decks are not empty play a round
		player1_card = deck_one.pop()						
		player2_card = deck_two.pop()

		str1 = str(player1_card[0]) + '_of_' + str(player1_card[1]) + '.png'
		str2 = str(player2_card[0]) + '_of_' + str(player2_card[1]) + '.png'
		image1 = pyglet.resource.image('cards/' + str1)
		image2 = pyglet.resource.image('cards/' + str2)
		image1.width = imageWidth
		image1.height = imageHeight
		image2.width = imageWidth
		image2.height = imageHeight
			
		if player1_card[0] != player2_card[0]:						#if the value of cards are not equal
			if player1_card[0] > player2_card[0]:					#if p1s is greater than p2s value
				player1_pile.append(player1_card)    				#p1 gets takes both cards
				player1_pile.append(player2_card)
			else:
				player2_pile.append(player1_card)					#if not, then p2 is > and gets both cards.
				player2_pile.append(player2_card)	
		
		
		else:														#if value of cards is equal
			war(deck_one, deck_two, player1_card, player2_card, player1_pile, player2_pile)		#War it out
				
	else:		
		deck_one = deck_one + player1_pile					#Then add your pile to your deck
		deck_two = deck_two + player2_pile
		random.shuffle(deck_one)								#Shuffle cards
		random.shuffle(deck_two)
		player1_pile = []
		player2_pile = []													#if not more cards in either's deck
		if len(deck_one) == len(deck_two):
			label = pyglet.text.Label('After Round 1 the Game is Tied', font_name='Times New Roman',font_size=25, x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')
		else:
			if len(deck_one) > len(deck_two):
				label = pyglet.text.Label('The Winner of Round 1 is Player1', font_name='Times New Roman',font_size=25, x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')
			else:
				label = pyglet.text.Label('The Winner of Round 1 is Player2', font_name='Times New Roman',font_size=25, x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center')
		
				
@window.event
def on_key_press(symbol, modifiers):
"""
Invocation: Key(symbol, modifiers).
Meaning: Pressing a key plays a new turn within the round.
Preconditions: A key needs to be pressed.
Postconditions: The returned value is the key pressed.
"""	
	play_one_turn(deck_one, deck_two)
	
@window.event
def on_draw():							#Used to show turn within round by pressing a key
"""
Invocation: Draw
Meaning: This function creates a window and draws the images of cards from our deck.
Preconditions: Images are png files taken from a folder.
Postconditions: The functions creates a window and then draws images.
"""
	window.clear()
	if len(deck_one) == 0 and len(deck_two) == 0:
		label.draw()
	elif player1_card[0] != player2_card[0]:
		image1.blit(150,300)
		image2.blit(400,300)
	else:
		image1.blit(150,300)
		image2.blit(400,300)
		image5.blit(150,250)
		image6.blit(150,200)
		image7.blit(150,150)
		image8.blit(400,250)
		image9.blit(400,200)
		image10.blit(400,150)
		
		image3.blit(150,100)
		image4.blit(400,100)
		
pyglet.app.run()
