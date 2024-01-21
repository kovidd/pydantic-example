import pytest
from contextlib import nullcontext as does_not_raise
from custom_validator import CustomUser, ic


def get_data(name="whatever", email="forge@blue.com", phone=5555):
    """
    Takes in optional parameters and returns a data dict

    Args
    """
    return locals()


@pytest.mark.parametrize(
    "key, expectation, expected_error",
    [
        ({"phone": -1234}, pytest.raises(Exception), "ValidationError"),
        ({"phone": "123f"}, pytest.raises(Exception), "ValidationError"),
        ({"phone": 1234}, does_not_raise(), True),
        ({"phone": "1234"}, does_not_raise(), True),
        ({"email": "1234"}, pytest.raises(Exception), "ValidationError"),
        ({"email": "john@doe.com"}, does_not_raise(), True),
        ({"name": 1234}, pytest.raises(Exception), "ValidationError"),
        ({"name": "john"}, does_not_raise(), True),
    ],
)
def test_custom_validator(key, expectation, expected_error):
    """
    Check all possible positive and negative tests together using parametrize

    Args:
        key (dict): overrides default data_dict in get_data
        expectation (error): pytest error type
        expected_error (str|bool): type of error
    """
    data = get_data(**key)
    with expectation as e:
        CustomUser(**data)
    if e:
        assert e.typename == expected_error
    else:
        assert expected_error
