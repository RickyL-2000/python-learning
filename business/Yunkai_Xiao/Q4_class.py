import random
import time

class Poker:
    def __init__(self):
        self._A = ['C','D','H','S']
        self._B = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        self.pokers = []
        n = 1
        for i in self._A:
            for j in self._B:
                self.pokers.append((n, (i+j)))
                n += 1
        random.shuffle(self.pokers)

    def deal(self, num, verbose=True):
        """deal cards to the player

        Args:
            num (int): the number of cards
        Returns:
            cards (List): list of cards for the player
        """
        cards = random.sample(self.pokers, num)
        for card in cards:
            self.pokers.remove(card)
            if verbose:
                print(card[1], ' ', end='')
        if verbose:
            print()
        return cards

    def sort_cards(self, cards, verbose=True):
        cards.sort()
        if verbose:
            for card in cards:
                print(card[1], ' ', end='')
            print()
        return cards

if __name__ == '__main__':
    poker = Poker()
    time.sleep(3)
    cards = poker.deal(13)
    cards = poker.sort_cards(cards)
    time.sleep(3)
    print("13张扑克牌（无大小王牌）")
    