from pydantic import BaseModel, EmailStr, field_validator
from icecream import ic


class CustomUser(BaseModel):
    name: str
    email: EmailStr
    phone: int

    @field_validator("phone")
    def valdate_phone_positive(cls, value):
        """Phone number should be positive int

        Args:
            cls, values

        Raises:
            ValueError: Phone number must be positive

        Returns:
            Any: value
        """
        if value <= 0:
            raise ValueError(f"Phone number must be positive: {value}")
        return value


if __name__ == "__main__":
    # example of email string validation
    user1 = CustomUser(name="whateverany", email="what@evs.com", phone=1327)
    ic(user1)

    # example of unwrapping dict and using for object creation
    data = {"name": "whomsoever", "email": "whom@evs.com", "phone": 1123}
    user2 = CustomUser(**data)
    ic(user2)

    # JSON SERIALIZATION
    # pydantic can convert objects to str
    user2_json_str = user2.json()
    ic(user2_json_str)

    # PYTHON DICT
    # pydantic can convert objects to dict
    user2_json_obj = user2.dict()
    ic(user2_json_obj)

    # CONVERT JSON STR TO JSON
    # pydantic can convert json string to json objects
    data_str = '{"name":"whichever", "email":"which@evs.com", "phone":5421}'
    user3 = CustomUser.parse_raw(data_str)
    ic("Make new user")
    ic(user3)
    user3_json_obj = user3.dict()
    ic(user3_json_obj)

    # dataclasses can do the above using: as.dict()
