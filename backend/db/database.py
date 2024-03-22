import sqlite3
import hashlib
import secrets
from .models import Car

def register_user(username, password):
    conn = sqlite3.connect("car_booking.db")
    cur = conn.cursor()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    api_key = secrets.token_urlsafe(16)
    try:
        cur.execute("INSERT INTO users (username, password_hash, api_key) VALUES (?, ?, ?)",
                     (username, password_hash, api_key))
        conn.commit()
        return True, "User registered successfully.", api_key
    except sqlite3.IntegrityError:
        return False, "Username already exists.", None
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("car_booking.db")
    cur = conn.cursor()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("SELECT id, api_key FROM users WHERE username=? AND password_hash=?", (username, password_hash))
    user = cur.fetchone()
    conn.close()
    if user:
        return True, "Login successful.", user[1]
    else:
        return False, "Invalid username or password.", None

def get_available_cars():
    conn = sqlite3.connect("car_booking.db")
    cur = conn.cursor()
    cur.execute("SELECT make, model, year, price FROM cars WHERE available=1")
    cars_data = cur.fetchall()
    conn.close()
    cars = [Car(make, model, year, price) for make, model, year, price in cars_data]
    return cars

def book_car(api_key, car_index):
    conn = sqlite3.connect("car_booking.db")
    cur = conn.cursor()
    cur.execute("SELECT make, model, year, price FROM cars WHERE available=1")
    cars_data = cur.fetchall()
    if not (1 <= car_index <= len(cars_data)):
        conn.close()
        return False, "Invalid car index."
    
    selected_car = cars_data[car_index - 1]
    cur.execute("INSERT INTO bookings (user_id, car_make, car_model, car_year, booking_date) VALUES (?, ?, ?, ?, CURRENT_DATE)",
                    (authenticate_api_key(api_key), selected_car[0], selected_car[1], selected_car[2]))
    cur.execute("UPDATE cars SET available=0 WHERE make=? AND model=? AND year=?", (selected_car[0], selected_car[1], selected_car[2]))
    conn.commit()
    conn.close()
    return True, f"Car booked successfully: {selected_car[0]} {selected_car[1]}"

def get_user_bookings(user_id, api_key):
    conn = sqlite3.connect("car_booking.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE api_key=?", (api_key,))
    auth_user_id = cur.fetchone()
    if not auth_user_id or auth_user_id[0] != user_id:
        conn.close()
        return False, "Unauthorized access.", None
    
    cur.execute("SELECT car_make, car_model, car_year, booking_date FROM bookings WHERE user_id=?", (user_id,))
    bookings_data = cur.fetchall()
    conn.close()
    if bookings_data:
        return True, "User bookings fetched successfully.", bookings_data
    else:
        return True, "No bookings found.", []
