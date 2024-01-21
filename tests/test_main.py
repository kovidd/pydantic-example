# ExceptionInfo class
# https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=exceptioninfo#exceptioninfo

import pytest

from contextlib import nullcontext as does_not_raise
from main import User, ic


# name tests
@pytest.mark.parametrize(
    "name_data, name_expected",
    [("whomsoever", "whomsoever"), ("spiral", "spiral")],
)
def test_main_names(name_data, name_expected):
    data = {"name": name_data, "email": "whom@evs.com", "phone": 7823}
    user_obj = User(**data)
    assert user_obj.name == name_expected


def test_main_names_negative():
    data = {"name": 123, "email": "whom@evs.com", "phone": 7823}
    with pytest.raises(Exception) as e:
        User(**data)
    assert e.typename == "ValidationError"


# email tests
@pytest.mark.parametrize(
    "email_data, expected_error",
    [("whomsoever@jinja.com", True), ("forgerock@blue.com", True)],
)
def test_main_email(email_data, expected_error):
    data = {"name": "whatever", "email": email_data, "phone": 7823}
    with does_not_raise():
        User(**data)
    assert expected_error


@pytest.mark.parametrize(
    "email_data, expected_error",
    [
        ("whomsoever.com", "ValidationError"),
        ("forgerock@blue", "ValidationError"),
    ],
)
def test_main_email_negative(email_data, expected_error):
    data = {"name": "whatever", "email": email_data, "phone": 7823}
    with pytest.raises(Exception) as e:
        User(**data)

    assert str(e.typename) == expected_error


# phone tests
@pytest.mark.parametrize(
    "phone, expectation, expected_error",
    [
        ("-123g", pytest.raises(Exception), True),
        ("123f", pytest.raises(Exception), True),
        ("1234", does_not_raise(), True),
    ],
)
def test_main_phone(phone, expectation, expected_error):
    data = {"name": "whatever", "email": "forge@blue.com", "phone": phone}
    with expectation as e:
        User(**data)
    assert expected_error
