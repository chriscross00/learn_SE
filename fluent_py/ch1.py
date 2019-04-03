import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class French_deck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                         for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')

deck = French_deck()

suit_values = dict(clubs = 0, diamonds = 1, hearts = 2, spades = 3)

def rank_cards(card):
    rank_value = French_deck.ranks.index(card.rank)


