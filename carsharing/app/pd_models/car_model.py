import re
from app import Base
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel, validator, ValidationError, Field


class Car(BaseModel):
    sign: str
    mark: str = Field(default='Reno', title='Поле содержит марку автомобиля', min_length=1)
    price_at_minute: float

    @validator('sign')
    def check_sign(cls, v:str) -> str:
        if re.match(r'/^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}$/ui', v)==None:
            raise ValueError ('Неправильный номер')
        return v


    @validator('mark')
    def check_mark(cls, v: str) -> str:
        if v != 'Skoda,Octavia' or 'Nissan, Qashqai' or 'Cherry, Tiger 7PRO':
            raise ValueError ('Такой машины не существует')
        return v

    @validator('price_at_minute')
    def check_price(cls, v: int) -> int:
        if v < 5.0 or v > 20:
            raise ValueError('Недопустимая цена')
        return v






