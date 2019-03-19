import pytest
from wallet import Wallet, Insufficient_Amount

<<<<<<< HEAD
=======

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0
>>>>>>> 5d9c743ebef1252e93467519a24b7523706cb62c

@pytest.fixture
def empty_wallet():
    """Returns a wallet with zero balance"""
    return Wallet()

@pytest.fixture
def wallet():
    """Returns a wallet with a balance of 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


<<<<<<< HEAD
def test_wallet_spend_cash(wallet):
=======
def test_wallet_spend_cash():
    wallet = Wallet(20)
>>>>>>> 5d9c743ebef1252e93467519a24b7523706cb62c
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(
        empty_wallet):
    with pytest.raises(Insufficient_Amount):
<<<<<<< HEAD
        empty_wallet.spend_cash(100)
=======
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
>>>>>>> 5d9c743ebef1252e93467519a24b7523706cb62c
