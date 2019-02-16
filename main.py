import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

# global variable to save our access_token
access = None
# storing this url for use to set permissions
auth = "https://connect.smartcar.com/oauth/authorize?response_type=code&client_id=69b1e512-8797-40a3-ac74-27c9f26cf75a&scope=read_vehicle_info+control_security+control_security:unlock+read_odometer+control_security:lock&redirect_uri=http://localhost:8000/vehicle&state=0facda3319&mode=live"

client = smartcar.AuthClient(
    client_id="69b1e512-8797-40a3-ac74-27c9f26cf75a",
    client_secret="6a29fc0d-3263-4f3e-ba7b-2c9acaa8e260",
    redirect_uri="http://localhost:8000/exchange",
    scope=['read_vehicle_info', 'read_odometer', 'control_security', 'control_security:unlock', 'control_security:lock'],
    test_mode=False
)


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
    return '', 200


@app.route('/vehicle', methods=['GET'])
def vehicle():
    # access our global variable to retrieve our access tokens
    global access
    # the list of vehicle ids
    vehicle_ids = smartcar.get_vehicle_ids(
        access['access_token'])['vehicles']

    # instantiate the first vehicle in the vehicle id list
    vehicle = smartcar.Vehicle(vehicle_ids[0], access['access_token'])
    info = ''
    try:
        info = vehicle.info()
        print(info)
        print("Permissions " + str(vehicle.permissions()))
        print("Odometer " + str(vehicle.odometer()))
    except TypeError:
        pass

    return jsonify(info)


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
