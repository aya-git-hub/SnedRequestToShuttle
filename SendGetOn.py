import requests

def sendGetOn(id,address):
    url = "http://localhost:8080/addPassenger"
    params = {
        "SUID": id,
        "address": address
    }

    try:
        # 发送 GET 请求
        response = requests.get(url, params=params)

        # 检查响应状态码并打印结果
        if response.status_code == 200:
            print("Passenger added successfully:", response.text)
        else:
            print(f"Failed to add passenger. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
