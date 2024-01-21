# https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf
# another example - https://github.com/ArjanCodes/2021-pydantic/blob/main/example.py
# pip install git+https://github.com/pydantic/pydantic@main#egg=pydantic[email]

from pydantic import BaseModel, EmailStr
from icecream import ic


class User(BaseModel):
    name: str
    email: EmailStr
    phone: int


if __name__ == "__main__":
    # example of email string validation
    user1 = User(name="whateverany", email="what@evs.com", phone=1327)
    ic(user1)

    # example of unwrapping dict and using for object creation
    data = {"name": "whomsoever", "email": "whomevs@d.com", "phone": 7821}
    user2 = User(**data)
    ic(user2)
