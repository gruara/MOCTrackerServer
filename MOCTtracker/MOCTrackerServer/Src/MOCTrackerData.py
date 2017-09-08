'''
Created on 21 Jul 2017

@author: Andrew Gruar
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
    
    SQL="""SELECT * 
           FROM moctracker.tracks 
           WHERE id = %s;"""
    data = (track_id, )
    cur.execute(SQL, data)
  
    if cur.rowcount == 1:
        row = cur.fetchone()
        track = buildTrack(row)
    else:
        track = None
        
    db.close
    return track

def getTracks(user_id):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
     
    cur = db.cursor()
    
    SQL = """SELECT * 
             FROM moctracker.tracks 
             WHERE user_id = %s;"""
    data = (user_id, )
    cur.execute(SQL, data )
    if cur.rowcount > 0:
        rows = cur.fetchall()
        tracks = []
        for row in rows:    
            track = buildTrack(row)
            tracks.append(track)
    else:
        tracks = None
        
    db.close
    return tracks



def insertTrack(inTrack):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
    cur = db.cursor()
    SQL = """INSERT INTO moctracker.tracks 
                (user_id,
                 created_on) 
             VALUES (%s, %s) 
             RETURNING id;"""
    data = (inTrack['user_id'], inTrack['created_on'])
    cur.execute(SQL, data)
#    yy=cur.mogrify(SQL, data)
#    zz=cur.statusmessage
#    print(yy)
#    print(zz)
    id = cur.fetchone()[0]
    db.commit()
    db.close
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
    SQL = """SELECT id,
                    user_id,
                    name,
                    created_on, 
                    password 
             FROM moctracker.users 
             WHERE user_id = %s;"""
    data = (userid, )
    cur.execute(SQL, data)
#     yy=cur.mogrify(SQL, data)
#     print(yy)
#     print (cur.rowcount)
    if cur.rowcount == 1:
        row = cur.fetchone()
        user = buildUser(row)
    else:
        user = None
        
    db.close
    return user

def insertUser(inUser):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)   
    cur = db.cursor()
    SQL = """INSERT INTO moctracker.users 
                (user_id, 
                 name, 
                 created_on) 
             VALUES (%s, %s, %s) 
             RETURNING id;"""
    data = (inUser['user_id'], inUser['name'], inUser['created_on'])
    cur.execute(SQL, data)
#     yy=cur.mogrify(SQL, data)
#     zz=cur.statusmessage
#     print(yy)
#     print(zz)
    id = cur.fetchone()[0]

    db.commit()
    db.close
    return

def updateToken(user_id, token):
    expiry = datetime.datetime.now() + datetime.timedelta(minutes=1440)
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)  
    if isinstance(user_id, str):
        userid = user_id
    else:
        userid = str(user_id, 'utf-8')
 
    cur = db.cursor()
    SQL = """UPDATE moctracker.users 
             SET token = %s, 
                 token_expiry = %s 
             WHERE user_id = %s;"""
    data = (str(token), str(expiry), userid)
    cur.execute(SQL, data)
#     yy=cur.mogrify(SQL, data)
#     zz=cur.statusmessage
#     print(yy)
#     print(zz)
    db.commit()
    db.close
    return

def updatePassword(user_id, password_hash):
    try:
        db = psycopg2.connect(connect)
    except:
        raise ("Unable to connect to the database", 500)  
    if isinstance(user_id, str):
        userid = user_id
    else:
        userid = str(user_id, 'utf-8')
 
    cur = db.cursor()
    SQL = """UPDATE moctracker.users 
             SET password = %s 
             WHERE user_id = %s;"""
    data = (str(password_hash), userid)
    cur.execute(SQL, data)
#     yy=cur.mogrify(SQL, data)
#     zz=cur.statusmessage
#     print(yy)
#     print(zz)
    db.commit()
    db.close
    return

def getSession(token):

    db = psycopg2.connect(connect)
    cur = db.cursor()
    SQL = """SELECT  user_id, token_expiry 
             FROM moctracker.users 
             WHERE token = %s;"""
    data = (str(token), )
    cur.execute(SQL, data)
#     yy=cur.mogrify(SQL, data)
#     print(yy)
#     print (cur.rowcount)
    if cur.rowcount == 1:
        row = cur.fetchone()
        session = buildSession(row)
    else:
        session = None
    db.close
    return session
   

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

def buildSession(row):
    token_expiry = row[1].strftime('%Y-%m-%d %H:%M:%S')
    
    session = {
            'user_id' : row[0],
            'token_expiry' : token_expiry,
        }
#    print(row[4])
    return session


if __name__ == '__main__':
    pass    