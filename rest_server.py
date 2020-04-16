from flask import Flask, jsonify, request
from query_database import get_avg_ratings_db, close_db, get_byod_db, get_contract_plans_db
import signal

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/avg_rating/', methods=['GET'])
def get_avg_ratings():
    # jsonify function that allows us to convert lists and dictionaries to JSON format.
    ratings = None
    if 'city_name' in request.args:
        city_name = request.args['city_name']
        ratings = get_avg_ratings_db(city_name=city_name)
        print(ratings)
    return jsonify(ratings)


@app.route('/byod', methods=['GET'])
def get_byod_data():
    byod_data = get_byod_db()
    print('Fetched {} plans for BYOD '.format(len(byod_data['plans'])))
    return jsonify(byod_data)


@app.route('/contracts', methods=['GET'])
def get_contract_based():
    contracts = get_contract_plans_db()
    print('Fetched {} plans for Contract based '.format(len(contracts['plans'])))
    return jsonify(contracts)


app.run(host='0.0.0.0', port='8000')
