from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime

from app.models import Permission
from app import db, redis


def data_json():
    json_data = request.get_json(force=True)
    if(not json_data):
        return jsonify({'message': 'No input data provided'}), 400   
    return json_data

class Permission_add(Resource):
    
    def post(self):
        json_data = data_json()
        per = Permission(email = json_data["email"],
                            level = json_data["level"])
        db.session.add(per)
        db.session.commit()
        return 200
    