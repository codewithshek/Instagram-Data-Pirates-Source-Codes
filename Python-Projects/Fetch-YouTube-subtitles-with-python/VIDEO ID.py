def get_video_id(videoURL):
    # split YouTube URL by '/' so we can get its ID
    videoID = str(videoURL).split('/')
    # get the last part of the list which is the ID
    videoID = videoID[-1]
    return videoID