import flask_login
from app import db
from flask_login import UserMixin


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(100), nullable=False)
    hometown = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __repr__(self):
        return f"Player(name={self.name}, birthday={self.birthday}, position={self.position}, grade={self.grade}, hometown={self.hometown})"


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    coach = db.Column(db.String(100), nullable=False)
    players = db.relationship('Player', backref='team', lazy=True)
    team_stats = db.relationship('TeamStats', backref='team', lazy=True)

    def __repr__(self):
        return f"Team(name={self.name}, coach={self.coach})"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    player_stats = db.relationship('PlayerStats', backref='user', lazy=True)
    team_stats = db.relationship('TeamStats', backref='user', lazy=True)

    def __repr__(self):
        return f"User(username={self.username}, is_admin={self.is_admin})"


class PlayerStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stat_type = db.Column(db.String(100), nullable=False)
    stat_value = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"PlayerStats(player_id={self.player_id}, user_id={self.user_id}, stat_type={self.stat_type}, stat_value={self.stat_value})"


class TeamStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stat_type = db.Column(db.String(100), nullable=False)
    stat_value = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"TeamStats(team_id={self.team_id}, user_id={self.user_id}, stat_type={self.stat_type}, stat_value={self.stat_value})"
