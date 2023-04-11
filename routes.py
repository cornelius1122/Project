from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from logger import logger
from models import Player, Team, User
from app import app, db

CORS(app)

# Get all players
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    result = [{'id': player.id,
               'name': player.name,
               'birthday': player.birthday.strftime('%m/%d/%Y'),
               'position': player.position,
               'grade': player.grade_year,
               'hometown': player.hometown} for player in players]
    return jsonify(result)


# Get a specific player by ID
@app.route('/players/<int:id>', methods=['GET'])
def get_player(id):
    player = Player.query.get_or_404(id)
    result = {'id': player.id,
              'name': player.name,
              'birthday': player.birthday.strftime('%m/%d/%Y'),
              'position': player.position,
              'grade': player.grade_year,
              'hometown': player.hometown}
    return jsonify(result)


# Create a new player
@app.route('/players', methods=['POST'])
def create_player():
    data = request.json
    name = data.get('name')
    birthday = data.get('birthday')
    position = data.get('position')
    grade = data.get('grade')
    hometown = data.get('hometown')

    if not all(field in data for field in ('name', 'birthday', 'position', 'grade', 'hometown')):
        return jsonify({'message': 'All fields are required'}), 400

    try:
        datetime.strptime(birthday, '%Y-%m-%d')

    except ValueError:
        logger.debug('Debug message')
        return jsonify({'message': 'Invalid date format'}), 400

    player = Player(name=name, birthday=birthday, position=position, grade_year=grade, hometown=hometown)
    db.session.add(player)
    db.session.commit()
    return jsonify({'message': 'Player created successfully!'}), 201


# Update an existing player
@app.route('/players/<int:id>', methods=['PUT'])
def update_player(id):
    player = Player.query.get_or_404(id)
    data = request.json
    player.name = data['name']
    player.birthday = datetime.strptime(data['birthday'], '%Y-%m-%d')
    player.position = data['position']
    player.grade_year = data['grade']
    player.hometown = data['hometown']
    db.session.commit()
    return jsonify({'message': 'Player updated successfully!'})


# Delete an existing player
@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    player = Player.query.get_or_404(id)
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player deleted successfully!'})
