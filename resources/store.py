from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.store import StoreModel


class Store(Resource):

    @jwt_required()
    def get(self, name):    
        store = StoreModel.get_item_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store does not exists'}, 404

    def post(self, name):
        if StoreModel.get_item_by_name(name):
            return {'message':'Store Already exists'}
        store = StoreModel(name)
        store.save_item()
        return store.json(),201

    def delete(self, name):
        store = StoreModel.get_item_by_name(name)
        if store:
            store.delete_item()
        return {'message':'store was succesfully deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
