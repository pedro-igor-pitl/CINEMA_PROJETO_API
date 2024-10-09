from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.String(64))
    release_date = db.Column(db.Date)
    duration = db.Column(db.Integer)  # in minutes
    description = db.Column(db.Text)

class Showtime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    cinema_hall = db.Column(db.String(64), nullable=False)
    movie = db.relationship('Movie', backref='showtimes')

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'))
    seat_number = db.Column(db.String(5))
    is_available = db.Column(db.Boolean, default=True)
    showtime = db.relationship('Showtime', backref='seats')

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtime.id'))
    total_price = db.Column(db.Float)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)
    seats = db.Column(db.String(128))  # comma-separated list of seat numbers
