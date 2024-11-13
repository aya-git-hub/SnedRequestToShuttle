from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

from SendRequest import sendRequest
from SendGetOn import sendGetOn
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

current_location = {"longitude": None, "latitude": None}
@app.route('/shuttleLocation', methods=['GET'])
def shuttle_location():
    global current_location
    # get the request number
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')

    if longitude and latitude:
        # update the location when receiving http request from shuttle service
        current_location["longitude"] = float(longitude)
        current_location["latitude"] = float(latitude)
        print(f"Updated shuttle position - Longitude: {longitude}, Latitude: {latitude}")
        return jsonify({"status": "success", "message": "Location received"}), 200
    else:
        return jsonify({"status": "error", "message": "Missing parameters"}), 400

#Map to <h1>Request for shuttle</h1>
@app.route('/send_request', methods=['POST'])
def send_request():
    # get SUID
    suid = request.form['suid']
    # send request to evening shuttle service
    sendRequest(suid)
    # then, redirect to main page
    return redirect(url_for('index'))

@app.route('/location')
def location():
    # map to location.html
    return render_template('location.html')

@app.route('/getCurrentLocation', methods=['GET'])
def get_current_location():
    return jsonify(current_location)

if __name__ == '__main__':
    app.run(port=5000, debug=True,use_reloader=False)