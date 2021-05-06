import moviepy.editor as mp
import os

def convert_video(path,outfile,ext='mp4'):
    clip = mp.VideoFileClip(path)
    upath = os.path.join(f"recordings/{outfile}_cleaned.{ext}")
    clip.write_videofile(upath)
    os.unlink(path)
    return upath
    