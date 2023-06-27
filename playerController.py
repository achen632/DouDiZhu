from player import Player

class playerController:
    def __init__(self, p1, p2, p3, deck, landlordPile):
        self.players = []
        self.players.append(Player(p1))
        self.players.append(Player(p2))
        self.players.append(Player(p3))
        self.deck = deck
        self.landlordPile = landlordPile
        self.currentPlayer = 0
        self.playerToBeat = 0
        self.cardsToBeat = []

    def addCard(self, index, card):
        self.players[index].addCard(card)

    def addCards(self, index, cards):
        self.players[index].addCards(cards)

    def clearHand(self):
        for player in self.players:
            player.clearHand()

    def printResults(self):
        self.players.sort(reverse=True)
        results = ""
        results += "1st: " + self.players[0].name + " (" + str(self.players[0].score) + ")\n"
        results += "2nd: " + self.players[1].name + " (" + str(self.players[1].score) + ")\n"
        results += "3rd: " + self.players[2].name + " (" + str(self.players[2].score) + ")"
        print(results)

    def printCardsToBeat(self):
        string = ""
        if not self.cardsToBeat:
            string += "还没有人出牌！该你表演了！"
        else:
            string += "上家(" + self.getPlayer(self.playerToBeat).name + ")出了: "
            for card in self.cardsToBeat:
                string += str(card) + " "
        print(string)

    def getPlayer(self, index):
        return self.players[index]

    def isFirstToPlay(self):
        return self.cardsToBeat == []

    def sortHand(self):
        for player in self.players:
            player.sortHand()

    def __str__(self):
        string = ""
        for p in self.players:
            string += str(p) + "\n"
        return string
    
    def bid(self):
        highestBidder = -1
        multiplier = 1
        # Cycle through all the players, starting with the winner of the previous round
        for i in range(3):
            p = self.players[(self.currentPlayer + i) % 3]
          
            # Print the player's hand
            print(p)

            # If a player has two jokers or 3+ twos AND nobody has bidden yet, they must bid
            if highestBidder == -1 and p.mustBid():
                input(p.name + "，你拍太强了！你必须当地主！")
                highestBidder = (self.currentPlayer + i) % 3
                multiplier *= 2
            else:

                # Get user input
                userInput = input(p.name + "，你要当地主吗？？(Y/N): ").lower()

                # Check if input is valid
                while True:

                    # If user passes, move on to next player
                    if userInput == "n" or userInput == "no":
                        break

                    # If user bids, update the current bidder double the multiplier
                    elif userInput == "y" or userInput == "yes":
                        highestBidder = (self.currentPlayer + i) % 3
                        multiplier *= 2
                        break

                    # Reprompt user if input is invalid
                    else:
                        userInput = input("对不起，我不明白。你要当地主吗？(Y/N): ")

        return highestBidder, multiplier
    
    def isRoundOver(self):
        numPassed = 0
        for player in self.players:
            if player.passed:
                numPassed += 1
        return numPassed == 2
    
    def isValidInput(self, input):
        # TODO split input and check each token
        return True
    
    def getCurrentPlayer(self):
        return self.players[self.currentPlayer]
    
    def updateCurrentPlayer(self):
        self.currentPlayer = (self.currentPlayer + 1) % 3
        while self.players[self.currentPlayer].passed:
            self.currentPlayer = (self.currentPlayer + 1) % 3
    
    def playCards(self, input):
        # Clear cardsToBeat
        self.cardsToBeat.clear()

        # Update playerToBeat
        self.playerToBeat = self.currentPlayer

        message = self.getCurrentPlayer().name + "出了"
        for c in input:
            # Get cards from input
            for card in self.getCurrentPlayer().hand:
                if str(card) == c:
                    # Remove cards from player's hand
                    self.getCurrentPlayer().hand.remove(card)
                    # Update cardsToBeat
                    self.cardsToBeat.append(card)
                    # Add the card played to the message
                    message += str(card) + " "
                    break

        # Print the cards played
        print(message + "!\n")
        
        # TODO implement bomb boolean return value
        return False
