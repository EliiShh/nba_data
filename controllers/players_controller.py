from flask import Blueprint, jsonify, request
from repository.players_repository import find_all_players_position_adn_season, find_all_players_position, \
    find_all_players

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/", methods=['GET'])
def get_players_by_position():
    positions = ['C', 'PF', 'SF', 'SG', 'PG']
    position = request.args.get('position')
    season = request.args.get('season')
    if not position or position not in positions:
        return jsonify({"error": "Position is not in of C, PF, SF, SG, PG."}), 400
    try:
        if season:
            players = find_all_players_position_adn_season(position, int(season))
            return jsonify(players), 200
        players = find_all_players_position(position)
        return players
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@players_blueprint.route("/all", methods=['GET'])
def get_all_players():
    try:
        players = find_all_players()
        return jsonify(players), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

