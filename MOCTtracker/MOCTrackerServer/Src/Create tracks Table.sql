set search_path = 'MOCTracker';

DROP SEQUENCE IF EXISTS tracks_id_seq;

CREATE SEQUENCE tracks_id_seq;

DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks (
  id integer not null  primary key,

  user_id varchar(250) ,
  created_on date 

);