from flask import Blueprint, request, jsonify

from repository.team_repository import delete_dream_team, find_all_dream_teams
from service.team_service import *

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route('/', methods=['POST'])
def create_team():
    data = request.json
    team_name = data.get('team_name')
    player_ids = data.get('player_ids')
    try:
        team_id = dream_team_from_controller_to_db(team_name, player_ids)
        return jsonify({'team_id': team_id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@teams_blueprint.route('/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.json
    player_ids = data.get('player_ids')
    try:
        team = update_team_from_controller_to_db(team_id, player_ids)
        return jsonify({"team update": team}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@teams_blueprint.route('/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    try:
        delete_dream_team(team_id)
        return jsonify({'STATUS':"deleted"}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@teams_blueprint.route('/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = team_with_player_details(team_id)
    if team:
        return jsonify(team), 200
    else:
        return jsonify({"error": 'not found'}), 404

@teams_blueprint.route('/compare', methods=['GET'])
def compare_teams():
    team1_id = request.args.get('team1')
    team2_id = request.args.get('team2')
    print(type(team1_id))
    print(type(team2_id))

    if team1_id is None or team2_id is None:
        return jsonify({"error": "plise gave to teams id"}), 400
    try:
        teams = comparison_between_teams(team1_id, team2_id)
        print(teams)
        return jsonify(teams), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@teams_blueprint.route('/', methods=['GET'])
def find_all_team():
    try:
        teams = find_all_dream_teams()
        return jsonify({"teams": teams}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400