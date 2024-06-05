from .database import db

class SongRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(100), nullable=False)
    requester_name = db.Column(db.String(100), nullable=False)

