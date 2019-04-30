import pytest
import rps


def test_game_dict():
    assert list(rps.rps_dict.keys())[0] == 'Rock'
    assert list(rps.rps_dict.keys())[1] == 'Paper'
    assert list(rps.rps_dict.keys())[2] == 'Scissors'

# learn how to test a input
#def test_valid_player_choice():
#    player = 'Rock'
#    assert rps.player_choice(player) ==
