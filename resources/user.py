from models.user import UserModel
from flask_restful import Resource, reqparse
import sqlite3

class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field can not be left blank'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field can not be left blank'
    )

    def post(self):
        data = UserRegistration.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'user already exists '}, 400

        user = UserModel(data['username'],data['password'])
        user.save_to_db()

        return {'message': 'User was registered succesfully'}, 201

    


