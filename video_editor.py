from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.resize import resize
import os

directory = ""
files = os.listdir(directory)

# Select half of the video clips
num_clips = len(files)
one_third = num_clips // 3
video1 = files[:one_third]
video2 = files[one_third:one_third*2]
video3 = files[one_third * 2:]


def join_video_clips(clips, output_path):
    # Load each video clip using VideoFileClip
    video_clips = [VideoFileClip(os.path.join(directory, clip)) for clip in clips]
    
    # Print height and width of each video clip
    for clip in video_clips:
        print(f"Video: {clip.filename}")
        print(f"Height: {clip.h}")
        print(f"Width: {clip.w}")
        print("")   

    #Resize the videos
    resolution = (1280, 720)  # Specify the desired resolution
    resized_clips = [clip.resize(resolution) for clip in video_clips]

    # Concatenate the video clips into a single longer video
    final_clip = concatenate_videoclips(resized_clips)

    # Write the final concatenated video to the output path
    final_clip.write_videofile(output_path)

# Join the clips into a single longer video
output_path1 = ""
output_path2 = ""
output_path3 = ""

join_video_clips(video1, output_path1)
join_video_clips(video2, output_path2)
join_video_clips(video3, output_path3)

# Delete all files in the directory
for file in files:
    file_path = os.path.join(directory, file)
    os.remove(file_path)