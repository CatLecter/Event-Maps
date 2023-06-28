from pydantic import BaseModel, Field, validator
from werkzeug.security import generate_password_hash


class User(BaseModel):
    email: str
    password: str
    login: str
    full_name: str
    phone: str
    photo: str = Field(default='https://proverit-cheloveka.loxotrona.net/images/default-profile-picture.jpg')
    latitude: float
    longitude: float
    role: str = Field(default='user')

    @validator('password')
    def hash_password(cls, item):
        return generate_password_hash(item)


class UserLogin(BaseModel):
    email: str
    password: str
