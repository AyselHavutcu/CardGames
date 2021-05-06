import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#Deck class will create 52 instances of Card class

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card =Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        #when we remove a card ,we need to remove it from the top just as the game required
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        #when we add a card ,we need to add a card to the bottom ust as the game required
        if(type(new_cards) == type([])):#if we have list of cards
            self.all_cards.extend(new_cards) #the extend method is for preventing a list to be added as nested list
        else:
            #for single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return 'Player {}  has {} cards.'.format(self.name,len(self.all_cards))

#create the players
player_one = Player('John')
player_two = Player('Marrie')

#create a deck of cards and shuffle them
new_deck = Deck()
new_deck.shuffle()

#share the cards between players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:

    #count the rounds
    round_num += 1
    print("Round {}".format(round_num))

    #check for the players cards 

    if len(player_one.all_cards) == 0:
        print("Player ONE is out of cards.Player TWO Wins!")
        game_on = False
        break
    #check for the player 2
    if len(player_two.all_cards) == 0:
        print("Player TWO is out of cards.Player ONE Wins!")
        game_on = False
        break
    
    #START A NEW ROUND
    player_one_cards = [] #played cards
    player_one_cards.append(player_one.remove_one()) #remove the card from the top and play with it

    player_two_cards = [] 
    player_two_cards.append(player_two.remove_one()) 
    
    #check if the players are war

    at_war = True

    while at_war:

        if player_one_cards[-1].value  > player_two_cards[-1].value:
            #then player one gets the all cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
    
        elif player_one_cards[-1].value  < player_two_cards[-1].value:
            #then player two gets the all cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        
        else:
            print("WAR!")
            #the cards are equal then they are at war check if the player's cards are out of range number
            if len(player_one.all_cards) < 5:
                print("Player ONE cannot declare war.Player TWO Wins!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print("Player TWO cannot declare war.Player ONE Wins!")
                game_on = False
                break
            else:
                #continue the game 
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

                       