
import pytest


@pytest.mark.client_a
def test_paypal_payment():
    pass


@pytest.mark.client_a
@pytest.mark.client_b
def test_credit_card_payment():
    pass


@pytest.mark.client_b
def test_apple_pay_payment():
    pass


