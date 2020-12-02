import ast
import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd


app = Flask(__name__)
api = Api(app)


class Users(Resource):

    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        args = parser.parse_args()

        # read our CSV
        data = pd.read_csv('users.csv')

        if args['userId'] in list(data['userId']):
            user_data = data[data['userId'] == args['userId']]
            user_index = user_data.index
            data.drop(user_index, inplace=True)
            data.to_csv('users.csv', index=False)
            return {'data': data.to_dict()}, 200

        else:
            return {
                'message': '{} user not found'.format(args['userId'])
            }, 404

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        parser.add_argument('locations', required=True)
        args = parser.parse_args()

        # read our CSV
        data = pd.read_csv('users.csv')

        if args['userId'] in list(data['userId']):
            # evaluate strings of lists to list
            data['locations'] = data['locations'].apply(
                lambda x: ast.literal_eval(x)
            )
            # select our user
            user_data = data[data['userId'] == args['userId']]

            # update user's locations
            user_data['locations'] = user_data['locations'].values[0].append(args['locations'])

            # save back to CSV
            data.to_csv('users.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        else:
            return {
                'message': '{} user not found.'.format(args['userId'])
            }, 404

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)

        args = parser.parse_args()

        # read our data
        data = pd.read_csv('users.csv')

        if args['userId'] in list(data['userId']):

            return {
                'message': '{} already exists'.format(args['userId'])
            }, 401

        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'userId': args['userId'],
                'name': args['name'],
                'city': args['city'],
                'locations': [[]]
            })

        # add the newly provided values
        data = data.append(new_data, ignore_index=True)

        # save back to CSV
        data.to_csv('users.csv', index=False)
        return {'data': data.to_dict()}, 200

    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        return {'data': data}


class Locations(Resource):
    pass


api.add_resource(Users, '/users') # '/users' is our entry point for Users
api.add_resource(Locations, '/locations') # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

