k# /mnt/data/routes.py

from flask import request, jsonify
from models import db, SongRequest, Event
from run import app
from marshmallow import Schema, fields

class SongRequestSchema(Schema):
    id = fields.Int(dump_only=True)
    song_name = fields.Str(required=True)
    artist = fields.Str(required=True)
    requested_by = fields.Str(required=True)
    event_id = fields.Int(required=True)

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    date = fields.DateTime(required=True)
    location = fields.Str(required=True)

song_request_schema = SongRequestSchema()
event_schema = EventSchema()

@app.route('/requests', methods=['POST'])
def add_song_request():
    data = request.get_json()
    errors = song_request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_request = SongRequest(
        song_name=data['song_name'],
        artist=data['artist'],
        requested_by=data['requested_by'],
        event_id=data['event_id']
    )
    db.session.add(new_request)
    db.session.commit()
    return song_request_schema.jsonify(new_request), 201

@app.route('/requests/<int:event_id>', methods=['GET'])
def get_song_requests(event_id):
    requests = SongRequest.query.filter_by(event_id=event_id).all()
    return song_request_schema.jsonify(requests, many=True)

@app.route('/events', methods=['POST'])
def add_event():
    data = request.get_json()
    errors = event_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_event = Event(
        name=data['name'],
        date=data['date'],
        location=data['location']
    )
    db.session.add(new_event)
    db.session.commit()
    return event_schema.jsonify(new_event), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return event_schema.jsonify(events, many=True)

