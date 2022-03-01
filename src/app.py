"""
    main app
"""
from flask import Flask
from src.auth.auth import auth_blueprint

app = Flask(__name__)

# register blueprint
app.register_blueprint(auth_blueprint)


@app.route("/")
def hello_world():
    """
    root route
    """
    return "<p>Hello, World!</p>"
