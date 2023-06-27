from deck import Deck
from playerController import playerController
from card import Card

deck = Deck()
gameActive = True
matchActive = True
landlordPile = []
players = None

# Prints greeting, gets user names, and creates playerController
def init():
    # Print greeting and get user names
    print("欢迎！希望你今天跟二王很有缘！")
    # TODO gets user input
    # p1 = input("请输入P1的名字: ")
    # p2 = input("请输入P2的名字: ")
    # p3 = input("请输入P3的名字: ")
    p1 = "p1"
    p2 = "p2"
    p3 = "p3"

    # Create playerController and pass names, deck, and landlordPile
    global players
    players = playerController(p1, p2, p3, deck, landlordPile)

# Set up the the game by shuffling and redealing cards
def setup():
    # Clear players' hands
    players.clearHand()

    # Shuffle cards
    deck.shuffle()

    # Deal cards and sort each hand
    for i in range(52):
        players.addCard(i % 3, deck.cards[i])
    players.sortHand()
    
    # Place remaining 3 cards into landlord pile
    landlordPile.clear()
    for i in range(51, 54):
        deck.cards[i].player = None
        landlordPile.append(deck.cards[i])

    # Sort landlord pile
    landlordPile.sort(key = Card.getPower)

# Prompts user if they want to play again
def playAgain():
    # TODO remove these lines and uncomment the lines below
    global gameActive
    gameActive = False
    # userInput = input("要再来一局吗？(Y/N): ").lower()
    # while True:
    #     if userInput == "n" or userInput.lower() == "no":
    #         global gameActive
    #         gameActive = False
    #         break
    #     elif userInput == "y" or userInput.lower() == "yes":
    #         break
    #     else:
    #         userInput = input("对不起，我不明白。要再来一局吗？(Y/N): ")

# Runs one round
def round():
    while True:
        # Cycle through the players (who haven't passed yet) in increasing order
        p = players.getCurrentPlayer()

        # Print greeting
        print(p.name + "，该你出牌了！")

        # Print cardsToBeat
        players.printCardsToBeat()

        # Print player's hand
        print(p)

        # Get input from player
        userInput = input("你要出什么牌？(输入'pass'跳过): ")

        while True:
            # If player passes update their status
            if userInput.lower() == "p" or userInput.lower() == "pass":
                # If the player is the first one to play, they cannot pass
                if players.isFirstToPlay():
                    print("你是第一个出牌的！你不能跳过！")
                    userInput = input("你要出什么牌？: ")
                    continue
                # Else, they pass and move onto the next player
                else:
                    p.passed = True
                    print(p.name + "不出！")
                    break
            # Check if the player's input is valid
            elif players.isValidInput(userInput):
                # Play cards
                isBomb = players.playCards(userInput)
                # If a bomb or rocket is played, double the multiplier
                if isBomb:
                    multiplier *= 2
                break
            # Reprompt the player if their input is invalid
            else:
                userInput = input("对不起，我不明白。你要出什么牌？(输入'pass'跳过): ")
        # If only one player remains in the round, they win the round and the round ends
        if players.isRoundOver():
            # Announce the winner
            print(players.players[players.currentPlayer].name + "赢了这一轮！")

            # Clear cardsToBeat
            players.cardsToBeat.clear()
            
            # End the round
            return
        
        # Move onto the next player
        players.updateCurrentPlayer()

# Runs the game
def run():
    # Players bid for landlord
    landlord, multiplier = players.bid()
    # If no one bids, reshuffle and deal again
    if landlord == -1:
        # Reveal landlord pile
        print("Landlord Pile: " + str(landlordPile[0]) + ", " + str(landlordPile[1]) + ", " + str(landlordPile[2]))
        print("没有人要当地主！重新发拍！\n")
        return

    # Reveal landlord pile
    print("\nLandlord Pile: " + str(landlordPile[0]) + ", " + str(landlordPile[1]) + ", " + str(landlordPile[2]))

    # Whoever one the bid becomes landlord and gets landlord pile
    # Announce landlord
    print(players.players[landlord].name + "是地主！准备好了吗？\n")
    players.players[landlord].addCards(landlordPile)

    # Begin round with the landlord playing first
    players.currentPlayer = landlord
    # while matchActive:
    round()
        # Set the winner of this round to become the first player in the next round
        # Reset all players' status to not passed
        # If one of the players have no cards they win

    # Update all players' scores
    playAgain()

# Prints the scoreboard in order of highest points
def results():
    print("\n###############")
    print("### RESULTS ###")
    print("###############")
    players.printResults()

if __name__ == "__main__":
    init()
    while gameActive:
        setup()
        run()
    results()