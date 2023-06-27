class Card:
    def __init__(self, power):
        self.power = power
        self.shuffle = None

    def __str__(self):
        if self.power == 8:
            return 'J'
        elif self.power == 9:
            return 'Q'
        elif self.power == 10:
            return 'K'
        elif self.power == 11:
            return 'A'
        elif self.power == 12:
            return '2'
        elif self.power == 13:
            return 'x'
        elif self.power == 14:
            return 'X'
        else:
            return str(self.power + 3)

    def getPower(card):
         return card.power
    
    def getValue(card):
        if card.power == 11:
            return -2
        elif card.power == 12:
            return -1
        elif card.power == 13:
            return -3
        elif card.power == 14:
            return -4
        else:
            return card.power
    
    def getShuffle(card):
        return card.shuffle