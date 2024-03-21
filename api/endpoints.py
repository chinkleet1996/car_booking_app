from flask import Flask, request, jsonify
from .models import Car, User
from ..db.database import authenticate_api_key, register_user, login_user, get_available_cars, book_car, get_user_bookings

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400
    
    success, message = register_user(username, password)
    status_code = 201 if success else 400
    return jsonify({"message": message}), status_code

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    success, message, user_id = login_user(username, password)
    status_code = 200 if success else 401
    return jsonify({"message": message, "user_id": user_id}), status_code

@app.route("/cars", methods=["GET"])
def get_available_cars():
    cars = get_available_cars()
    cars_data = [{"make": car.make, "model": car.model, "year": car.year, "price": car.price} for car in cars]
    return jsonify(cars_data), 200

@app.route("/book", methods=["POST"])
def book_car_endpoint():
    data = request.get_json()
    api_key = data.get("api_key")
    car_index = data.get("car_index")
    if not api_key or not car_index:
        return jsonify({"error": "API key and car index are required."}), 400

    user_id = authenticate_api_key(api_key)
    if not user_id:
        return jsonify({"error": "Invalid API key."}), 401

    success, message = book_car(user_id, car_index)
    status_code = 201 if success else 400
    return jsonify({"message": message}), status_code

@app.route("/bookings/<int:user_id>", methods=["GET"])
def get_user_bookings_endpoint(user_id):
    api_key = request.headers.get("X-API-Key")
    if not api_key:
        return jsonify({"error": "API key is required."}), 400
    
    auth_user_id = authenticate_api_key(api_key)
    if not auth_user_id or auth_user_id != user_id:
        return jsonify({"error": "Unauthorized access."}), 401

    bookings = get_user_bookings(user_id)
    if bookings:
        bookings_data = [{"make": booking.car_make, "model": booking.car_model, "year": booking.car_year, "booking_date": booking.booking_date} for booking in bookings]
        return jsonify(bookings_data), 200
    else:
        return jsonify({"message": "No bookings found."}), 200

