from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import User, Movie, Showtime, Seat, Booking
from flask_login import login_user, logout_user

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    movies = Movie.query.all()
    return render_template('home.html', movies=movies)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login form submission
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # Handle user registration
    return render_template('register.html')

@bp.route('/movies/<int:movie_id>')
def movie_details(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    showtimes = movie.showtimes
    return render_template('movie.html', movie=movie, showtimes=showtimes)

@bp.route('/book/<int:showtime_id>', methods=['GET', 'POST'])
def book_tickets(showtime_id):
    showtime = Showtime.query.get_or_404(showtime_id)
    available_seats = Seat.query.filter_by(showtime_id=showtime.id, is_available=True).all()
    
    if request.method == 'POST':
        selected_seats = request.form.getlist('seats')
        booking = Booking(
            user_id=current_user.id,
            showtime_id=showtime_id,
            total_price=len(selected_seats) * 13,  # Assume ticket price is 13
            seats=",".join(selected_seats)
        )
        db.session.add(booking)
        db.session.commit()
        flash('Booking successful!')
        return redirect(url_for('main.orders'))

    return render_template('booking.html', showtime=showtime, available_seats=available_seats)

@bp.route('/orders')
def orders():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('orders.html', bookings=bookings)
