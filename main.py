from flask import Flask

from controllers.players_controller import players_blueprint

from controllers.team_controller import teams_blueprint


app = Flask(__name__)

app.register_blueprint(players_blueprint, url_prefix="/api/players")
app.register_blueprint(teams_blueprint, url_prefix="/api/teams")


if __name__ == '__main__':
    app.run(debug=True)

# from seed.seed import seed
#
#
#
# if __name__ == '__main__':
#     seed()
#     app.run(debug=True)