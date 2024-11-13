import requests
from SendGetOn import sendGetOn
from Address import Address
import random

import json


def sendRequest(id):
    url = "http://localhost:8080/requestPickupBySuid"
    params = {"SUID": id}

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            #print(response.text[0])
            safe_text = response.text.encode('utf-8', errors='ignore').decode('utf-8')
            response_json = json.loads(safe_text)
            print("Response from server:", safe_text)
            target_text = '{"data":null,"errorMessage":"This student has already submitted the request and cannot submit it again."}'
            if safe_text != target_text:
                sendGetOn(id, Address.addresses[random.randint(0, 49)])

        else:
            print(f"Failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


