from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime

from app.models import Document
from app import db, redis

def verify_token(json):
    json_data = request.get_json()
    email = json_data["email"]
    token_verify = json_data["token"]
    token = redis.hget(email, "field1")
    return(token == token_verify)

def data_json():
    json_data = request.get_json(force=True)
    if(not json_data):
        return jsonify({'message': 'No input data provided'}), 400   
    return json_data    

class Document_CRUD(Resource):
    
    

    def get(self):
        pass

    def post(self):
        json_data = data_json()
        if(verify_token(json_data)):
            return jsonify({'message': 'token wrong'}), 400
        document = Document(name= json_data["name"],
                                category= json_data["category"],
                                user= json_data["user_id"],
                                avaliado= False,
                                directory = json_data["directory"])
        db.session.add(document)
        db.session.commit()
        return 200

    def put(self):
        json_data = data_json()
        if(verify_token(json_data)):
            return jsonify({'message': 'token wrong'}), 400
        document = Document.query.filter_by(name=json_data["name"])
        document.name = json_data["name"]
        document.category = json_data["category"]
        db.session.add(document)
        db.session.commit()
        return 200

    def delete(self):
        json_data = data_json()
        if(verify_token(json_data)):
            return jsonify({'message': 'token wrong'}), 400
        document = Document.query.filter_by(name=json_data["name"])
        db.session.delete(document)
        db.session.commit()
        return 200