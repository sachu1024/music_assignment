from musicapp import db,app
from sqlalchemy.orm import relationship
import datetime

class Music_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, unique_key=True)
    song_name = db.Column(db.String(100),nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    created_date = db.Column(db.String(100),nullable=False)
 
    

    def __init__(self,song_id,song_name,duration,created_date):
        self.song_id  = song_id
        self.song_name=song_name
        self.duration=duration
        self.created_date=created_date

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pod_id = db.Column(db.String(100),unique_key=True)
    pod_name = db.Column(db.String(100),nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    upload_time = db.Column(db.String(100),nullable=False)
    host = db.Column(db.String(100),nullable=False)
    participant= db.Column(db.String(100),nullable=False)
    

    def __init__(self,pod_id,pod_name,duration,upload_time,host,participant):
        self.pod_id  = pod_id
        self.pod_name=pod_name
        self.duration=duration
        self.upload_time=upload_time
        self.host=host
        self.participant=participant

class Audio(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    audio_id=db.Column(db.String(100),unique_key=True)
    audio_title=db.Column(db.String(225),nullable=False)
    narrator=db.Column(db.String(100),nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    upload_time = db.Column(db.String(100),nullable=False)

    def __init__(self,audio_id,audio_title,narrator,duration,upload_time):
        self.audio_id=audio_id
        self.audio_title=audio_title
        self.narrator=narrator
        self.duration=duration
        self.upload_time=upload_time


        