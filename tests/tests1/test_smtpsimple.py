import pytest


@pytest.fixture
def smtp_connection():
    """docstring for smtp_connection"""
    import smtplib

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    """docstring for test_ehlo"""
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0
