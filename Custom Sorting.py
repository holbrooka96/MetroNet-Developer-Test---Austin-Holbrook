import random
#Create card object that has a value and a suit
class Card:
    def __init__(self, value, suit):
            self.suit = suit
            self.value = value

#Create deck object that initializes values and suits, creates, and shuffles the deck of cards.
class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts','Diamonds', 'Clubs', 'Spades']
        
    def __init__(self):
        self.cards = []
        self.create()
        
    def create(self):
        for i in range(len(self.suits)):
            for j in range(len(self.values)):
                self.cards.append(Card(self.values[j], self.suits[i]))
    
    def print(self):
        for i in self.cards:
            print(i.value, 'of', i.suit)
    
    def shuffle(self):
        for i in range(len(self.cards)):
            num = random.randint(0,i)
            x = self.cards[i]
            self.cards[i] = self.cards[num]
            self.cards[num] = x


#Create hand object that draws five cards from the deck object and reorders them either ascending or descending.
class Hand(Deck):
    def __init__(self, num_of_cards):
        self.num_of_cards = num_of_cards
        self.cards = []

    def draw(self, deck):
        for i in range(self.num_of_cards):
            self.cards.append(deck.cards.pop())
    
    #Set descending to 1 when calling the method to sort descending.        
    def sort(self, descending = 0):
        for i in range(self.num_of_cards):
            for j in range(self.num_of_cards):
                try:
                    if self.values.index(self.cards[j].value) > self.values.index(self.cards[j+1].value):
                        x = self.cards[j+1]
                        self.cards[j+1] = self.cards[j]
                        self.cards[j] = x
                except:
                    continue
        
        for i in range(self.num_of_cards):
            for j in range(self.num_of_cards):
                try:
                    if self.values.index(self.cards[j].value) == self.values.index(self.cards[j+1].value) and self.suits.index(self.cards[j].suit) > self.suits.index(self.cards[j+1].suit):
                        x = self.cards[j+1]
                        self.cards[j+1] = self.cards[j]
                        self.cards[j] = x
                except:
                    continue 
        if descending:
            self.cards.reverse()

d = Deck()
d.shuffle()
h = Hand(5)
h.draw(d)
h.sort(1)
print('=====================')
h.print()
