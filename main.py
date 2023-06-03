import json

from flask import Flask, jsonify
from api.reports import api_bp
from api.ticket_handler import api_th

app = Flask(__name__)

app.register_blueprint(api_bp)
app.register_blueprint(api_th)


if __name__ == '__main__':
    app.run(debug=True)


