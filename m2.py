from moviepy.editor import VideoFileClip, ImageClip
clip = VideoFileClip("19edit.mp4")
fps= 100.0 # take one frame per second
nframes = clip.duration*fps # total number of frames used
total_image = sum(clip.iter_frames(fps,dtype=float,logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image.save_frame("19edit2.png")
