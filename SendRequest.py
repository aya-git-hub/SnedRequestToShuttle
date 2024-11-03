import requests
from SendGetOn import sendGetOn

def sendRequest(id):
    url = "http://localhost:8080/requestPickupBySuid"
    params = {"SUID": id}

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            #print(response.text[0])
            safe_text = response.text.encode('utf-8', errors='ignore').decode('utf-8')
            print("Response from server:", safe_text)
            sendGetOn(id, "123 elm st, Syracuse, 13210")
        else:
            print(f"Failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


