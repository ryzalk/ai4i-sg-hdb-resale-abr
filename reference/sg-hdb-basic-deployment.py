"""
DO NOT RUN THIS CELL!
"""

from flask import Flask
from flask_restful import reqparse, Api, Resource
import pickle
import numpy as np

app = Flask(__name__)
api = Api(app)

# specify location of pickled model and load it
file_loc_name = '../models/sg_hdb_lm_v1.pkl'
sg_hdb_loaded_model = pickle.load(open(file_loc_name, 'rb'))

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

class PredictResalePrice(Resource):
    def get(self):

        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        
        user_floor_area_sqm = np.array(float(user_query))
        user_floor_area_sqm_reshaped = user_floor_area_sqm.reshape(-1, 1)
        user_resale_price = sg_hdb_loaded_model.predict(user_floor_area_sqm_reshaped)

        # create JSON object
        output = {'prediction': user_resale_price[0]}
        #output = user_resale_price
        
        return output

# Setup the API resource routing here
# Route the URL to the resource
api.add_resource(PredictResalePrice, '/')

if __name__ == "__main__":
    app.run(debug=True)