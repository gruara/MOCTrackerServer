'''
Created on 20 Jul 2017

@author: Andrew
'''
from flask import Flask, abort, request, jsonify
from flask import abort
import MOCTrackerApp
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Go away'

@app.route('/MOCTracker/api/v1.0/tracks', methods=['GET'])
def get_all():
#    resp = 'You going to get it all'
    tracks = MOCTrackerApp.getTracks()
    return tracks

@app.route('/MOCTracker/api/v1.0/tracks/<int:track_id>', methods=['GET'])
def get_track(track_id):
    try:
        track = MOCTrackerApp.getTrack(track_id)
    except:
        abort(404)
        
    return track
    
@app.route('/MOCTracker/api/v1.0/tracks', methods=['POST'])
def insert_track():
    inTrack=request.get_json(force=True)
#    print(inTrack)
    try:
        resp = MOCTrackerApp.insertTrack(inTrack)
    except:
        return 
    return "Inserted"
 
@app.route('/MOCTracker/api/v1.0/tracks/<int:account>', methods=['POST'])
def update_track(account):
#    xx = request.json
    return "I've been upputted" 

@app.route('/MOCTracker/api/v1.0/users/<string:user_id>', methods=['GET'])
def get_user(user_id):

    try:
        track = MOCTrackerApp.getUser(user_id)
    except:
        abort(404)
        
    return track

@app.route('/MOCTracker/api/v1.0/users', methods=['POST'])
def insert_user():
    inUser=request.get_json(force=True)
#    print(inTrack)
    try:
        resp = MOCTrackerApp.insertUser(inUser)
    except:
        return 
    return "Inserted"

    
 
if __name__ == '__main__':
    app.run(debug=True)