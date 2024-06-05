# /mnt/data/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SongRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    requested_by = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    def __repr__(self):
        return f"<SongRequest {self.song_name} by {self.artist}>"

    def serialize(self):
        return {
            'id': self.id,
            'song_name': self.song_name,
            'artist': self.artist,
            'requested_by': self.requested_by,
            'event_id': self.event_id
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    song_requests = db.relationship('SongRequest', backref='event', lazy=True)

    def __repr__(self):
        return f"<Event {self.name} at {self.location}>"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date.isoformat(),
            'location': self.location
        }

