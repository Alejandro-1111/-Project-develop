from http import client
from wsgiref import headers
from iot_device import Sensor
import json
import time

# creating the object for the http conection
conn = client.HTTPConnection(host="localhost", port=5000)

# class sensor
s = Sensor()

# simulate the sensor 
headers = {'Content-type': 'application/json'}

while True:
    data = {
    "id": 1,
    "name": "Temp_sensor",
    "value": s.get_random_number()
    }
    
    json_data = json.dumps(data)

    if data["value"] >= 15:
        print(f'Warnign: the device is upper {data["value"]} grades')
        conn.request("POST", "/devices", json_data, headers)
        conn.close()
    
    time.sleep(1)