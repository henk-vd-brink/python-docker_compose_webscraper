import requests
import json
from flask import Flask
from resources.tor_controller import TorController

app = Flask(__name__)

proxies = {"http": "privoxy:8118", "https": "privoxy:8118"}

@app.route('/get_new_ip_address')
def change_ip_address():
    TorController().change_ip()
    response_ip = requests.get("https://api.ipify.org?format=json", proxies=proxies).json()
    response_tor = requests.get("http://check.torproject.org", proxies=proxies).text
    current_ip_address = response_ip["ip"] 

    response_json = {}
    response_json["current_ip"] = current_ip_address
    response_json["tor_configured"] = str(True if "Congratulations" in response_tor else False)

    return json.dumps(response_json)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)





