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


from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = Vector(3, 4)

print(v1 * 2)
