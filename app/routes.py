from flask import Blueprint, request, jsonify
from .models import SongRequest
from .database import db

main = Blueprint('main', __name__)

@main.route('/request_song', methods=['POST'])
def request_song():
    data = request.get_json()
    song_name = data.get('song_name')
    requester_name = data.get('requester_name')
    new_request = SongRequest(song_name=song_name, requester_name=requester_name)
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'Petición recibida', 'song_name': song_name, 'requester_name': requester_name})

@main.route('/requests', methods=['GET'])
def get_requests():
    requests = SongRequest.query.all()
    output = [{'song_name': req.song_name, 'requester_name': req.requester_name} for req in requests]
    return jsonify(output)

