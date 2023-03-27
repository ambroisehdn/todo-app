import config

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DevelopmentConfig().SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = config.DevelopmentConfig().SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)


@cross_origin()
@app.route('/')
def index():
    return jsonify({"message": "flask app :) "})


if __name__ == '__main__':
    app.run(debug=config.DevelopmentConfig().FLASK_DEBUG)
