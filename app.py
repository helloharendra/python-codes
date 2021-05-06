import streamlit as st
from vision import view_cam,record
from db import Video
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from converter import convert_video

def opendb():
    engine = create_engine('sqlite:///db.sqlite3') # connect
    Session =  sessionmaker(bind=engine)
    return Session()

def save_file(path):
    try:
        db = opendb()
        file =  os.path.basename(path)
        name, ext = file.split('.') # second piece
        vid = Video(filename=name,extension=ext,filepath=path)
        db.add(vid)
        db.commit()
        db.close()
        return True
    except Exception as e:
        st.write("database error:",e)
        return False

btncam = st.button('view webcam output')
name_of_video = st.text_input('video name (without ext)',value='example_video')
btnrec = st.button('record webcam video')
if btncam:
    view_cam()

if btnrec:
    folder = 'recordings'
    path = os.path.join(folder,f"{name_of_video}.mp4")
    record(path)
    upath = convert_video(path,name_of_video)
    status = save_file(upath)
    if status:
        st.success("saved video")
    else:
        st.error("failed")

db = opendb()
videos=db.query(Video).all()
db.close()
vid = st.selectbox('select a video to play',videos)
if vid and os.path.exists(vid.filepath):
    st.video(vid.filepath)


