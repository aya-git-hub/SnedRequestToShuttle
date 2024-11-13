import requests

def sendGetOn(id,address):
    url = "http://localhost:8080/addPassenger"
    params = {
        "SUID": id,
        "address": address
    }

    try:
        # Send GET request
        response = requests.get(url, params=params)

        # Check the status code
        if response.status_code == 200:
            print("Passenger added successfully:", response.text)
        else:
            print(f"Failed to add passenger. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
