# -*- coding: utf-8 -*-
"""
Tutorial on using the InfluxDB client.
Original from https://influxdb-python.readthedocs.io/en/latest/examples.html
"""

import argparse

from influxdb import InfluxDBClient
import pprint
import json

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Avoid insecure warnings for because of verify_ssl=False with scalingo Influxdb
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




def main(host='localhost', port=8100:
    """Instantiate a connection to the InfluxDB."""
    user = 'user'
    password = 'pass'
    dbname = 'db'
    verify_ssl=False
    ssl = True
    query = 'select * from Device_dc2d_int WHERE time > \'2019-01-03 09:00:00\' AND time < \'2019-01-03 10:00:00\';'
    #Device_dc2d_int WHERE time > \'2018-12-29 09:00:00\' AND time < \'2019-01-05 19:00:00\';'
    #Device_test;'
    #Device_dc2d_int;'
    json_body = [
        {
            "measurement": measurement,
            "tags": {
                "deveui": deveui,
                "device_id": topic,
                "Nsensors": "1",
                "frequency": freq,
                "Channel": chan
            },
            "time": TStamp,
            "fields": {
                "A1": A1,
                "A2": A2,
                "A3": A3,
                "A4": A4,
                "A5": A5,
                "P1": P1,
                "P2": P2,
                "P3": P3,
                "Upcount": upcntr,
                "RSSI": RSSI,
                "SNR" : SNR,
                "SF" : SF,
                "Payload_cleartext": data,

            }
        }
    ]

    # json_body = [
    #     {
    #         "measurement": "cpu_load_short",
    #         "tags": {
    #             "host": "server01",
    #             "region": "us-west"
    #         },
    #         "time": "2009-11-10T23:00:00Z",
    #         "fields": {
    #             "Float_value": 0.64,
    #             "Int_value": 3,
    #             "String_value": "Text",
    #             "Bool_value": True
    #         }
    #     }
    # ]

    client = InfluxDBClient(host, port, user, password, dbname, ssl, verify_ssl)

    # print("Create database: " + dbname)
    # client.create_database(dbname)

    # print("Create a retention policy")
    # client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    # print("Switch user: " + dbuser)
    # client.switch_user(dbuser, dbuser_password)

    # print("Write points: {0}".format(json_body))
    # client.write_points(json_body)

    print("Querying data: " + query)
    result = client.query(query)

    #rs = cli.query("SELECT * from cpu")
    cpu_points = list(result.get_points(measurement='Device_dc2d_int'))
    data= json.dumps(cpu_points) 
    # print data

    for C in cpu_points:
        # print C['P2']
        #print C
        if C['P2']>8 :
            print C['time']
            print C['P2']

    # print("Write points: {0}".format(result))
    client.write_points(data)


    # rawjson=result.raw()
    #print cpu_points
    #print result
    # print "point ={0}".format(cpu_points)
    # print "items ={0}".format(item)
    # print "keys ={0}".format(keys)
    # print json.dumps(rawjson)

    # jdata = json.loads(result)
    # for c in jdata['children'][0]['children']:
    #     print 'Title: {}, URI: {}'.format(c.get('title', 'No title'),c.get('uri', 'No uri'))

    # print("Result: {0}".format(result))
    #print json.loads(result)

    # print("Switch user: " + user)
    # client.switch_user(user, password)

    # print("Drop database: " + dbname)
    # client.drop_database(dbname)


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8100
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)