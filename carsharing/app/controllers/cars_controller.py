from app import app, engine
from sqlalchemy.orm import Session
from app.pd_models.car_model import *

@app.post('/car/create', tags=['Автомобиль'])
def create_car(cars: Car):
    with Session(engine) as session:
        car = Car(mark = Car.mark, sign=Car.sign, price_at_minute=Car.price_at_minute)
        session.add(car)
        session.commit()
    
    return {'status': 'success'}


@app.put('/car/update', tags=['Автомобиль'])
def update_car(sign: Car.sign):
    with Session(engine) as session:
        car = session.query(Car).filter_by(sign=Car.sign).first()
        car = Car(mark=Car.mark, sign=Car.sign, price_at_minute=Car.price_at_minute)
        session.add(car)
        session.commit()
    return {}


@app.delete('/car/delete', tags=['Автомобиль'])
def delete_car(sign: Car.sign):
    with Session(engine) as session:
        car = session.query(Car).filter_by(sign=Car.sign).first()
        session.delete(car)
        session.commit()
    return {}


@app.get('/car/get', tags=['Автомобиль'])
def get_car(sign: Car.sign):
     with Session(engine) as session:
        car = session.query(Car).filter_by(sign=Car.sign).first()
        return {'mark': car.mark, 'sign': car.sign, 'price_at_minute': car.price_at_minute, 'users': car.users}
