import pytest
#import mock
import rps


def test_game_dict():
    assert list(rps.rps_dict.keys())[0] == 'Rock'
    assert list(rps.rps_dict.keys())[1] == 'Paper'
    assert list(rps.rps_dict.keys())[2] == 'Scissors'

"""
# learn how to test a input
def test_valid_player_choice(monkeypatch):

    monkeypatch.setattr('sys.stdin', lambda: 'Rock')
    assert rps.player_choice() == 'Rock'
"""

""""def test_mock():

    with mock.patch('builtins.input', return_value = 'Rock'):
        assert rps.player_choice() == 'Rock'"""
