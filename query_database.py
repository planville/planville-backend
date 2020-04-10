#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "root", "provider")

cursor = db.cursor()

# # fetchone() − It fetches the next row of a query result set.
# sql = """select * from employee"""
# rowcount = cursor.execute(sql)
# result = cursor.fetchone()
# print(result)


def get_avg_ratings_db(city_name):
    colors = ["#393E41", "#E94F37", "#1C89BF", "#A1D363",
              "#85FFC7", "#297373", "#FF8552", "#A40E4C"]
    sql = """select Provider, Reviews from provider.rating where City='{}' order by Reviews desc;""".format(city_name)
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    print("results: {}".format(results))
    ratings = []
    index = 0
    for name, radius in results:
        provider = {'name': name, 'radius': '{}px'.format(radius*50), 'color': colors[index]}
        index = index + 1
        ratings.append(provider)
    return ratings


def close_db():
    # disconnect from server
    print("Closing the database...")
    db.close()



