from . import db
from flask_login import UserMixin

# Intialize Task and User objects
class Task(db.Model):
    '''
    Task has foreign key link to User table
    '''
    __tablename__ = 'Task'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=True, unique=True, primary_key=True)
    status = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))



class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    task_id = db.relationship('Task', backref='User')