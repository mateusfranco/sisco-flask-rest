from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime

from app.models import Document
from app import db, redis


class Document_CRUD(Resource):
    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
