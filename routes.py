# /mnt/data/routes.py

from flask import request, jsonify
from models import db, SongRequest, Event
from run import app

@app.route('/requests', methods=['POST'])
def add_song_request():
    data = request.get_json()
    new_request = SongRequest(
        song_name=data['song_name'],
        artist=data['artist'],
        requested_by=data['requested_by'],
        event_id=data['event_id']
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'Request added!'}), 201

@app.route('/requests/<int:event_id>', methods=['GET'])
def get_song_requests(event_id):
    requests = SongRequest.query.filter_by(event_id=event_id).all()
    return jsonify([req.serialize for req in requests])

@app.route('/events', methods=['POST'])
def add_event():
    data = request.get_json()
    new_event = Event(
        name=data['name'],
        date=data['date'],
        location=data['location']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event added!'}), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.serialize for event in events])

