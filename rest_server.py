from flask import Flask, jsonify, request
from query_database import get_avg_ratings_db, close_db
import signal

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/avg_rating/', methods=['GET'])
def get_avg_ratings():
    # jsonify function that allows us to convert lists and dictionaries to JSON format.
    rating = None
    if 'city_name' in request.args:
        city_name = request.args['city_name']
        ratings = get_avg_ratings_db(city_name=city_name)
        print(ratings)
    return jsonify(ratings)


app.run(port='8000')
