'''
Created on 20 Jul 2017

@author: Andrew Gruar
'''
from flask import Flask, abort, request, jsonify,  Response

import MOCTrackerApp
import json
from base64 import b64decode
from MOCTrackerApp import session

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Go away'

@app.route('/MOCTracker/api/v1.0/login', methods=['GET'])
def login():
#    print ('what here')
    authorization64 = request.headers.get('Authorization')
    authorization = b64decode(authorization64)

# b':' is used in split as getting error ' bytes-like object is required, not 'str'' without it'
    username, password = authorization.split(b':', 1)
    token = MOCTrackerApp.login(username, password)
    if token == None:
        abort(401)
    else:
        resp = Response('OK')
        resp.headers['Authorization'] = token
        return resp


@app.route('/MOCTracker/api/v1.0/login/<string:user_id>', methods=['PUT'])
def update_password(user_id):
#     token = request.headers.get('Authorization')
#     if MOCTrackerApp.checkToken(token) is False:
#         abort(401)
    changePass = request.get_json(force=True)
    updated_pass = MOCTrackerApp.changePassword(user_id, changePass)
    if updated_pass is None:
        abort(401)

    return updated_pass
    
    
@app.route('/MOCTracker/api/v1.0/tracks', methods=['GET'])
def get_all():
    token = request.headers.get('Authorization')
    if MOCTrackerApp.checkToken(token) is False:
        abort(401)
    
#    print(MOCTrackerApp.session['user_id'])
#    resp = 'You going to get it all'
    tracks = MOCTrackerApp.getTracks(MOCTrackerApp.session['user_id'])
    return tracks

@app.route('/MOCTracker/api/v1.0/tracks/<int:track_id>', methods=['GET'])
def get_track(track_id):
    token = request.headers.get('Authorization')
    if MOCTrackerApp.checkToken(token) is False:
        abort(401)

    track = MOCTrackerApp.getTrack(track_id)
    if track == None:
        abort(404)
    else:
        return track
    
@app.route('/MOCTracker/api/v1.0/tracks', methods=['POST'])
def insert_track():
    token = request.headers.get('Authorization')
    if MOCTrackerApp.checkToken(token) is False:
        abort(401)
    
    
    inTrack = request.get_json(force=True)
#    print(inTrack)
    try:
        resp = MOCTrackerApp.insertTrack(inTrack)
    except:
        return 
    return "Inserted"
 
@app.route('/MOCTracker/api/v1.0/tracks/<int:account>', methods=['PUT'])
def update_track(account):
#    xx = request.json
    return "I've been upputted" 

@app.route('/MOCTracker/api/v1.0/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    token = request.headers.get('Authorization')
    if MOCTrackerApp.checkToken(token) is False:
        abort(401)

    
    user = MOCTrackerApp.getUser(user_id)
    if user == None:
        abort(404)
    else:
        return user

@app.route('/MOCTracker/api/v1.0/users', methods=['POST'])
def insert_user():
    token = request.headers.get('Authorization')
    if MOCTrackerApp.checkToken(token) is False:
        abort(401)
    
    inUser = request.get_json(force=True)
#    print(inTrack)
    try:
        resp = MOCTrackerApp.insertUser(inUser)
    except:
        return 
    return "Inserted"

    
 
if __name__ == '__main__':
    app.run(debug=True)