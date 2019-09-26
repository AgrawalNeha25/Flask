from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This field can not be left blank'
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help='This field can not be left blank'
    )

    @jwt_required()
    def get(self, name):    
        item = ItemModel.get_item_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item does not exists'}, 404

    def post(self, name):
        if ItemModel.get_item_by_name(name):
            return {'message':'Item Already exists'}
        requested_data = Item.parser.parse_args()
        item = ItemModel(name,requested_data['price'],requested_data['store_id'])
        item.save_item()
        return item.json(),201

    def delete(self, name):
        item = ItemModel.get_item_by_name(name)
        if item:
            item.delete_item()
        return {'message':'item was succesfully deleted'}

    def put(self, name):
        requested_data = Item.parser.parse_args()
        item = ItemModel.get_item_by_name(name)
        if item:
            item.price = requested_data['price']
        else:
            item = ItemModel(name,requested_data['price'],requested_data['store_id'])
        item.save_item()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
