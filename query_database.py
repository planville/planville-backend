#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "root", "provider")

cursor = db.cursor()

sql = """SELECT * from provider.provider"""
cursor.execute(sql)
results = cursor.fetchall()
providers = {}
for id, name in results:
    providers[id] = name
print('Provider list: {}'.format(providers))


def get_avg_ratings_db(city_name):
    colors = ["#393E41", "#E94F37", "#1C89BF", "#A1D363",
              "#85FFC7", "#297373", "#FF8552", "#A40E4C"]
    sql = """select Provider, Reviews from provider.rating where City='{}' order by Reviews desc;""".format(city_name)
    print('Fetching Ratings from the Database: Query: {}'.format(sql))
    cursor.execute(sql)
    results = cursor.fetchall()
    ratings = []
    index = 0
    for name, radius in results:
        provider = {'name': name, 'radius': '{}px'.format(radius*50), 'color': colors[index]}
        index = index + 1
        ratings.append(provider)
    print('Ratings fetched and returned')
    return ratings


def get_byod_db():
    sql = """SELECT Price, Internet, idProvider, Offers, Talktime, URL from provider.byod;"""
    print('Fetching BYOD Plans from the Database: Query: {}'.format(sql))
    cursor.execute(sql)
    results = cursor.fetchall()
    byod = {'plans': []}
    for Price, Internet, idProvider, Offers, Talktime, URL in results:
        plan = {
            'Price': Price,
            'Internet': Internet,
            'Provider': providers[int(idProvider)],
            'Offers': Offers if Offers else '-',
            'Talktime': Talktime,
            'URL': URL
        }
        byod['plans'].append(plan)
    return byod


def get_contract_plans_db():
    sql = """SELECT * from provider.contract;"""
    print('Fetching Contract based Plans from the Database: Query: {}'.format(sql))
    cursor.execute(sql)
    results = cursor.fetchall()
    contracts = {'plans': []}
    for id, PhoneName, PhonePrice, DownPayment, idProvider, InternetGB, Talktime, Numofinstallments, URL, planPrice in results:
        plan = {
            'PhoneName': PhoneName,
            'PhonePrice': PhonePrice,
            'DownPayment': DownPayment,
            'Provider': providers[idProvider],
            'InternetGB': InternetGB,
            'Talktime': Talktime,
            'Numofinstallments': Numofinstallments,
            'URL': URL,
            'planPrice': planPrice
        }
        contracts['plans'].append(plan)
    return contracts


def close_db():
    # disconnect from server
    print("Closing the database...")
    db.close()



