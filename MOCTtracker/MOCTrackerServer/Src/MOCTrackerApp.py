'''
Created on 20 Jul 2017

@author: Andrew
'''

import MOCTrackerData
import json
from passlib.hash import pbkdf2_sha256

def login(username, password):
#    print (type(username))
    user=MOCTrackerData.getUser(username)
    if user == None:
        storedhash = None
    else:
        storedhash=user['password']
        if pbkdf2_sha256.verify(password, storedhash):
            print ('Password OK')
        else:
            storedhash = None
    
#    hash = pbkdf2_sha256.hash(password)
#    print (hash)
    return storedhash




def getTrack(track_id):
    try:
        track = MOCTrackerData.getTrack(track_id)
    except:
        raise
    response = json.dumps(track)
    return response

def getTracks():
    try:
        tracks = MOCTrackerData.getTracks()
    except:
        raise
    response = json.dumps(tracks)
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
    if user == None:
        respone = None
    else:
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