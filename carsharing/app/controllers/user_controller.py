from app import app, engine
from sqlalchemy.orm import Session
from app.pd_models.user_model import *
from app.data_models.user_db_model import *

@app.post('/user/create', tags=['Пользователь'])
def create_car(users: User):
    with Session(engine) as session:
        user = User(username=User.username, password_hash=User.password_hash)
        session.add(user)
        session.commit()

    return {'status': 'success'}


@app.put('/user/update', tags=['Пользователь'])
def update_car(username: User.username):
    with Session(engine) as session:
        user = session.query(User).filter_by(username=User.username).first()
        user = User(username=User.username, password_hash=User.password_hash)
        session.add(user)
        session.commit()
    return {}


@app.delete('/user/delete', tags=['Пользователь'])
def delete_car(username: User.username):
    with Session(engine) as session:
        user = session.query(User).filter_by(username=User.username).first()
        session.delete(user)
        session.commit()
    return {}


@app.get('/user/get', tags=['Пользователь'])
def get_car(username: User.username):
    with Session(engine) as session:
        user = session.query(User).filter_by(username=User.username).first()
        return {'username': user.username, 'password_hash': user.passwoed_hash}
