class Car:
    def __init__(self, make, model, year, price, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.available = available

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
