import moviepy
from moviepy.editor import *

vid = VideoFileClip("19.mp4")

newvid = vid.fx(vfx.invert_colors)


newvid.write_videofile("19edit.mp4")
