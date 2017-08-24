'''
Created on 21 Jul 2017

@author: Andrew
'''

import psycopg2
import datetime


connect = "dbname='MOCdb' user='MOC_andrew' host='//localhost' password='iolabr0n'"

def getTrack (track_id):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
     
    cur = db.cursor()
    
    SQL="SELECT * FROM moctracker.tracks WHERE id = %s;"
    data=(track_id, )
    cur.execute(SQL, data)
  
    if cur.rowcount == 1:
        row = cur.fetchone()
    else:
        raise ('Track not found', 404)
        
    track = buildTrack(row)
    return track

def getTracks ():
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
     
    cur = db.cursor()
    
    SQL="SELECT * FROM moctracker.tracks;"
#    data=(track_id, )
    cur.execute(SQL, )
    if cur.rowcount > 0:
        rows = cur.fetchall()
    else:
        raise ('Track not found', 404)
    tracks = []
    for row in rows:    
        track = buildTrack(row)
        tracks.append(track)
    return tracks



def insertTrack(inTrack):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
    cur = db.cursor()
    SQL="INSERT INTO moctracker.tracks (user_id, created_on) VALUES (%s, %s) RETURNING id;"
    data=(inTrack['user_id'], inTrack['created_on'])
    cur.execute(SQL, data)
#    yy=cur.mogrify(SQL, data)
#    zz=cur.statusmessage
#    print(yy)
#    print(zz)
    id=cur.fetchone()[0]
    db.commit()

    return

def getUser (user_id):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
#    print (type(user_id))
    if isinstance(user_id, str):
        userid = user_id
    else:
        userid = str(user_id, 'utf-8')
        
    cur = db.cursor()
    SQL="SELECT id, user_id, name, created_on, password FROM moctracker.users WHERE user_id = %s;"
    data=(userid, )
    cur.execute(SQL, data)
#     yy=cur.mogrify(SQL, data)
#     print(yy)
#     print (cur.rowcount)
    if cur.rowcount == 1:
        row = cur.fetchone()
        user = buildUser(row)
    else:
        user = None
        

    return user

def insertUser(inUser):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
    cur = db.cursor()
    SQL="INSERT INTO moctracker.users (user_id, name, created_on) VALUES (%s, %s, %s) RETURNING id;"
    data=(inUser['user_id'], inUser['name'], inUser['created_on'])
    cur.execute(SQL, data)
#    yy=cur.mogrify(SQL, data)
#    zz=cur.statusmessage
#    print(yy)
#    print(zz)
    id=cur.fetchone()[0]
    db.commit()

    return

def updateToken(user_id, token):
    expiry=datetime.datetime.now() + datetime.timedelta(days=1)
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)  
    if isinstance(user_id, str):
        userid = user_id
    else:
        userid = str(user_id, 'utf-8')
 
    cur = db.cursor()
    SQL="UPDATE moctracker.users SET token = %s, token_expiry = %s WHERE user_id = %s;"
    data=(str(token), str(expiry), userid)
    db.commit()
    return
    

def buildTrack(row):
    created_on = row[2].strftime('%Y-%m-%d %H:%M:%S')
    
    track = {
            'track_id': row[0],
            'user_id' : row[1],
            'created_on' : created_on

        }
    return track

def buildUser(row):
    created_on = row[3].strftime('%Y-%m-%d %H:%M:%S')
    
    user = {
            'id': row[0],
            'user_id' : row[1],
            'name' : row[2],
            'created_on' : created_on,
            'password' : row[4]
        }
#    print(row[4])
    return user

if __name__ == '__main__':
    pass    