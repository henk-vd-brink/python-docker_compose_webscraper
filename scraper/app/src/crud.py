import psycopg2
import requests
import json
import time

class Crud():
    _proxies={  "http": "http://localhost:8118",
                "https": "https://localhost:8118"  }
    
    def post_data(self, url, payload):
        payload = json.dumps(payload)
        response = requests.post(url, payload)
        print(f"Posted {url}: {response.text}.")
        return response

    def _get_html_from_url(self, url):
        for _ in range(0, 2):
            response = self.get_data(url)
            if response.status_code == 200:
                break
        else:
            response = self.change_ip()
            if response.status_code != 200:
                raise ConnectionRefusedError("Could not connect with Privoxy/Tor")
            response = self.get_data(url)
        return response.text
    
    def get_html(self, url):
        html = self._get_html_from_url(url)
        return html

    def get_data(self, url):
        try:
            response = requests.get(url, proxies = self._proxies)
        except Exception:
            return type("response", (), {"status_code": "50x"})
        else:
            print(f"Retrieved data from: {url}, {response.status_code}.")
            return response
    
    def change_ip(self):
        url = "http://localhost:5000/tor_controller"
        response = requests.post(url, "")
        return response

class MockCrud(Crud):

    def post_data(self, url, payload):
        print(f"post_data: {url}, {payload}")


