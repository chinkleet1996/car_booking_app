from flask import Flask
from api.endpoints import app

if __name__ == "__main__":
    app.run(debug=True)