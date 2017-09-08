'''
Created on 20 Jul 2017

@author: Andrew Gruar
'''

import MOCTrackerData
import json
import uuid
import datetime
from passlib.hash import pbkdf2_sha256

session = {}


def login(username, password):
#    print (type(username))
    user = MOCTrackerData.getUser(username)
    if user == None:
        token = None
    else:
        storedhash = user['password']
        if pbkdf2_sha256.verify(password, storedhash):
            token = uuid.uuid4()
#            print (type(token))
            MOCTrackerData.updateToken(username, token)
        else:
            token = None
    
#    hash = pbkdf2_sha256.hash(password)
#    print (hash)
    return token

def changePassword(user_id, passwords):
    user = MOCTrackerData.getUser(user_id)
    if user == None:
        passhash = None
    else:
        if user['password'] is None and passwords['old_password'] == '':
            passhash = pbkdf2_sha256.hash(passwords['new_password'])
        else:

            storedhash = user['password']
            if pbkdf2_sha256.verify(passwords['old_password'], storedhash):
                passhash = pbkdf2_sha256.hash(passwords['new_password'])
            else:
                passhash = None
    if passhash is not None:
        MOCTrackerData.updatePassword(user_id, passhash)
        passhash = 'Password updated'
    return passhash

def getTrack(track_id):
    try:
        track = MOCTrackerData.getTrack(track_id)
    except:
        raise
    if track is None:
        response = None
    else:
        response = json.dumps(track)
    return response

def getTracks(user_id):
    try:
        tracks = MOCTrackerData.getTracks(user_id)
    except:
        raise
    if tracks is None:
        response = None
    else:
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
    if user is None:
        response = None        
    else:
        response = json.dumps(user)
    return response

def insertUser(inUser):
    try:
        track = MOCTrackerData.insertUser(inUser)
    except:
        raise

    return 

def checkToken(token):
    global session
    
    session = MOCTrackerData.getSession(token)
    if session == None:
        return False

    if datetime.datetime.now() > \
       datetime.datetime.strptime(session['token_expiry'], 
                                          '%Y-%m-%d %H:%M:%S'):
        return False
    return True


if __name__ == '__main__':
    pass  