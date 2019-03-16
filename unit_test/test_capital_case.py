import pytest
import capital_case as cc


def test_capital_case():
    assert cc.make_capital('monday') == 'Monday'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        cc.make_capital(9)


print(cc.make_capital('hi'))
