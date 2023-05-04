import sqlalchemy.orm
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
app = FastAPI()


engine = create_engine('sqlite:///data.db')
Base = sqlalchemy.orm.declarative_base()


