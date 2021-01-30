from dotenv import load_dotenv
load_dotenv()

import keepalive
import subprocess
import os

import cv2


rtmp_url = f"rtmp://a.rtmp.youtube.com/live2/live2/{os.getenv('YT_STREAM_KEY')}"

fps = 12
width = 2560
height = 1440 

command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-pixel_format', 'bgr24',
           '-video_size', "{}x{}".format(width, height),
           '-framerate', str(fps),
           '-i', '-',
           '-re',
           '-f', 'mp3',
           '-stream_loop', '-1',
           '-i', 'audio.mp3',
           '-c:v', 'libx264',
           '-c:a', 'aac',
           '-vf', 'format=yuv420p',
           '-f', 'flv',
           '-preset', 'ultrafast',
           '-b:v', '15000k',
           '-maxrate', '6000k',
           '-bufsize', '3968k',
rtmp_url]

def run():
  p = subprocess.Popen(command,  stdin=subprocess.PIPE)

  while True:
    p.stdin.write(cv2.imread('banner.png').tobytes())
    line = p.stdout.readline()
    print(line)




run()