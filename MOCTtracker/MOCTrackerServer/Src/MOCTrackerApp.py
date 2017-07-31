'''
Created on 20 Jul 2017

@author: Andrew
'''

import MOCTrackerData
import json

def getTrack(track_id):
    try:
        track = MOCTrackerData.getTrack(track_id)
    except:
        raise
    response = json.dumps(track)
    return response

def insertTrack(inTrack):
    try:
        track = MOCTrackerData.insertTrack(inTrack)
    except:
        raise

    return 

def getUser(user_id):
    
    try:
        user = MOCTrackerData.getUser(user_id)
    except:
        raise
    response = json.dumps(user)
    return response

def insertUser(inUser):
    try:
        track = MOCTrackerData.insertUser(inUser)
    except:
        raise

    return 


if __name__ == '__main__':
    pass  