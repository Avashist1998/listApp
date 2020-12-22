from .extentions import sqlDB
from flask_login import UserMixin

class User(UserMixin, sqlDB.Model):
    id = sqlDB.Column(sqlDB.Integer, primary_key=True)
    email = sqlDB.Column(sqlDB.String(100), unique=True)
    password = sqlDB.Column(sqlDB.String(100))
    name = sqlDB.Column(sqlDB.String(100))