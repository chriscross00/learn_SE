import pytest
import rps

from random import Random


def test_game_dict():
    assert list(rps.rps_dict.keys())[0] == 'Rock'
    assert list(rps.rps_dict.keys())[1] == 'Paper'
    assert list(rps.rps_dict.keys())[2] == 'Scissors'


def test_valid_player_choice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'Rock')
    assert rps.player_choice() == 'Rock'


# Not sure how to test the game, research
def test_game(monkeypatch):

    computer = Random(50)

    player = 1
    monkeypatch.setattr('builtins.input', lambda x: 1)

    assert rps.game(player) == 'Draw'


def test_random():
    test_int = Random(50)
    assert test_int.randint(1, 3) == 2
