import math
import os

import smartcar
from flask import Flask, redirect, request, jsonify, url_for
from flask_cors import CORS

import strings

app = Flask(__name__)
CORS(app)

# global variable to save our access_token
access = None
# storing this url for use to set permissions
auth = "https://connect.smartcar.com/oauth/authorize?response_type=code&client_id=69b1e512-8797-40a3-ac74-27c9f26cf75a&scope=read_vehicle_info+control_security+control_security:unlock+read_odometer+control_security:lock&redirect_uri=http://localhost:8000/vehicle&state=0facda3319&mode=live"
fe = 'https://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2019&make=TESLA&model=Model%203'

client = smartcar.AuthClient(
    client_id="69b1e512-8797-40a3-ac74-27c9f26cf75a",
    client_secret="6a29fc0d-3263-4f3e-ba7b-2c9acaa8e260",
    redirect_uri="http://localhost:8000/exchange",
    scope=['read_vehicle_info', 'read_odometer', 'control_security', 'control_security:unlock', 'control_security:lock'],
    test_mode=True
)


@app.route('/')
def main_page():
    return redirect(url_for("login"))


@app.route('/login', methods=['GET'])
def login():
    auth_url = client.get_auth_url()
    return redirect(auth_url)


@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')

    # access our global variable and store our access tokens
    global access
    # in a production app you'll want to store this in some kind of
    # persistent storage
    access = client.exchange_code(code)
    print(access)
    return redirect(url_for("vehicle"), code=200)


@app.route('/vehicle', methods=['GET'])
def vehicle():
    # access our global variable to retrieve our access tokens
    global access
    # the list of vehicle ids
    vehicle_ids = smartcar.get_vehicle_ids(
        access['access_token'])['vehicles']

    vehicle_summary = strings.header
    for vid in vehicle_ids:
        # instantiate the first vehicle in the vehicle id list
        vehicle = smartcar.Vehicle(vid, access['access_token'])
        info = ''
        odometer = ''
        try:
            info = vehicle.info()
            odometer = vehicle.odometer()
        except TypeError:
            print("Failed to get info from vehicle %s" % vid)
            continue
        compound_name = info['make'] + info['model'] + str(info['year'])
        vehicle_summary += strings.card % (
            info['make'], info['model'],
            info['make'], info['model'], info['year'],
            math.floor(odometer['data']['distance'] * 0.000621371),
            63, 1284, 918,
            '#' + compound_name)
        vehicle_summary += strings.details_modal % (compound_name)
    vehicle_summary += strings.footer
    return vehicle_summary


@app.route('/unlock', methods=['GET'])
def unlock():
    global access
    vehicle_ids = smartcar.get_vehicle_ids(
        access['access_token'])['vehicles']
    vehicle = smartcar.Vehicle(vehicle_ids[0], access['access_token'])

    response = ''
    try:
        response = vehicle.unlock()
        print("Unlocked? " + ("True" if response is None else "False"))
    except smartcar.exceptions.PermissionException as e:
        print("Unlocked? Insufficient permissions")

    return "True" if response is None else "False"


if __name__ == '__main__':
    app.run(port=8000)
