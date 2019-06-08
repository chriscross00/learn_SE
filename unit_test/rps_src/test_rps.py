import pytest
import rps


def test_game_dict():
    assert list(rps.rps_dict.keys())[0] == 'Rock'
    assert list(rps.rps_dict.keys())[1] == 'Paper'
    assert list(rps.rps_dict.keys())[2] == 'Scissors'


def test_valid_player_choice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'Rock')
    assert rps.player_choice() == 'Rock'

