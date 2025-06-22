from flask_migrate import Migrate
from flask import Flask, jsonify, request
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from extensions import db
from models import Episode, Guest, Appearance

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def home():
    return {"message": "Welcome to the API!"}


@app.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict(rules=('-appearances',)) for e in episodes])


@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict())


@app.route('/guests')
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict(rules=('-appearances',)) for g in guests])


@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    guest = Guest.query.get(data.get('guest_id'))
    episode = Episode.query.get(data.get('episode_id'))

    if not guest or not episode:
        return jsonify({"errors": ["Guest or Episode not found"]}), 404

    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=guest.id,
            episode_id=episode.id,
            guest=guest,
            episode=episode
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400


if __name__ == '__main__':
    app.run(debug=True)
