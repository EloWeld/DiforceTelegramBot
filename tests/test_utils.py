
from handlers.req import search_objects
from utils import format_phone_number


def test_format_phone_number():
    phoneNumber = "89620788985"
    d = format_phone_number(phoneNumber)
    assert d == "+79620788985"
    