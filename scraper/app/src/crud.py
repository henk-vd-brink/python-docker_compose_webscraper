import psycopg2
import requests
import json

class Crud():

    
    
    def post_data(self, url, payload):
        response = requests.post(url, json.dumps(payload))
        return response.status_code

class MockCrud():

    def post_data(self, url, payload):
        print(url, payload)
