'''
Created on 21 Jul 2017

@author: Andrew
'''

import psycopg2


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
     
    cur = db.cursor()
    SQL="SELECT * FROM moctracker.users WHERE user_id = %s;"
    data=(user_id, )
    cur.execute(SQL, data)
#    yy=cur.mogrify(SQL, data)
#    print(yy)
    
    if cur.rowcount == 1:
        row = cur.fetchone()
    else:
        raise ('Track not found', 404)
        
    user = buildUser(row)
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
            'created_on' : created_on
        }
    return user

if __name__ == '__main__':
    pass    