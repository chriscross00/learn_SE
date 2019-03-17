import pytest
from wallet import Wallet, Insufficient_Amount


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(Insufficient_Amount):
        wallet.spend_cash(100)


# # Parametrized test function
# @pytest.mark.parametrize('earned, spent, expected', [
#     (30, 10, 20),
#     (20, 2, 18)
# ])
# def test_transactions(earned, spent, expected):
#     my_wallet = Wallet()
#     my_wallet.add_cash(earned)
#     my_wallet.spend_cash(spent)
#     assert my_wallet.balance == expected


# Combining fixtures and parametrized functions
@pytest.fixture
def my_wallet():
    """Returns a Wallet instance with a balance of zero"""
    return Wallet()


@pytest.mark.parametrize('earned, spent, expected', [
    (30, 10, 20),
    (10, 2, 8)
])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
