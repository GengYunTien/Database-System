# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'Player'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_ID = db.Column(db.Integer, nullable=False)
    player_name = db.Column(db.String(30), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    birth_place = db.Column(db.String(30), nullable=True)
    team_ID = db.Column(db.Integer, db.ForeignKey('Team.team_ID'))
    stats_ID = db.Column(db.Integer, db.ForeignKey('BattingStatistics.stats_ID'))

class Team(db.Model):
    __tablename__ = 'Team'
    team_ID = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)

class BattingStatistics(db.Model):
    __tablename__ = 'BattingStatistics'
    stats_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AVG = db.Column(db.Float)
    Hits = db.Column(db.Integer)
    HR = db.Column(db.Integer)
    RBI = db.Column(db.Integer)
