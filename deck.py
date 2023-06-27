import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(i))
        self.cards.append(Card(13))
        self.cards.append(Card(14))

    def __str__(self):
        string = ""
        for card in self.cards:
            string += str(card) + ", "
        return string
    
    def shuffle(self):
        for card in self.cards:
            card.shuffle = random.randint(0, 100)
        self.cards.sort(key=Card.getShuffle)