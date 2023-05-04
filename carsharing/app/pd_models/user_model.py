import re

from pydantic import BaseModel, validator, ValidationError, Field


class User(BaseModel):
    id: int
    first_name: str = Field(default='Василий')
    second_name: str

    @validator('first_name')
    def check_first_name(cls, v: str) -> str:
        if v[0].islower():
            raise ValueError ('Имя должно быть с заглавной буквы')
        return v

    @validator('second_name')
    def check_second_name(cls, v: str) -> str:
        if v[0].islower():
            raise ValueError('Фамилия должна быть с заглавной буквы')
        return v



