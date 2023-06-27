from card import Card

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.score = 0
        self.isLandlord = False
        self.passed = False

    def clearHand(self):
        self.hand.clear()

    def addCard(self, card):
        self.hand.append(card)

    def addCards(self, cards):
        self.hand += cards
        self.sortHand()

    def sortHand(self):
        self.hand.sort(key=Card.getValue)

    def __str__(self):
        string = ""
        for card in self.hand:
            string += str(card) + ", "
        return string
    
    def __lt__(self, other):
         return self.score < other.score
    
    def mustBid(self):
        for i in range(17):
            if self.hand[i].power == 14 and self.hand[i + 1].power == 13:
                return True
            elif self.hand[i].power == 12 and self.hand[i + 1].power == 12 and self.hand[i + 2].power == 12:
                return True
        return False