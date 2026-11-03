# pylint: disable=missing-docstring

from utils import Cli
from itertools import count


class EnglishAuction():

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
         # Input opening bid
         # au début, on garde le même schéma que celui de blind, en changeant le nom de l'enchère !!
        self.cli.display('Started auction of type: English')
        opening_bid = self.cli.prompt('Please enter the amount for the opening bid:')
        opening_bid = int(opening_bid)
        self.cli.display(f"Opening bid is: {opening_bid}")
        
                # Input bidders
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(f"Enter name for bidder {index} (enter nothing to move on):")
            if not bidder:
                    break
            bidders.append(bidder)
            self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")
        
                # Collect bids : ici ça change
        standing_bid = opening_bid
        winner = None
        someone_bid = True              #initialisation de la boucle while
        while someone_bid:              
            someone_bid = False         #on a fini, sauf si quelqu'un se prononce audesssus
            for bidder in bidders:
                bid = self.cli.prompt(f"Standing bid is {standing_bid}.")          #on reprend la typo de blind
                if bid is not None:
                    bid = int(bid)
                    if bid > standing_bid:          #on garde le même test
                        standing_bid = bid          # dans ce cas on a un nouveau gagnant pour un nouveau montant
                        winner = bidder
                        someone_bid = True          #on peut essayer un autre tour
        return winner, standing_bid             # ça ne marche pas : ça ne rend pas le couple
    
#bémols : on ne supprime pas les gens qui ne sont plus dans la course, et si c'est le premier qui enchérit 
# et les autres non, les autres vont devoir dire 2 fois non avant que l'enchère se termine.

if __name__ == "__main__":
    EnglishAuction().play()