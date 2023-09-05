import threading
import subprocess

def run_twitch_scraper():
    subprocess.run(["python", "C:/Users/twitch_scraper.py"])

def run_video_editor():
    subprocess.run(["python", "C:/video_editor.py"])

def run_youtube_uploader():
    subprocess.run(["python", "C:/Users/youtube_uploader.py"])

if __name__ == "__main__":
    # Create threads for running twitch_scraper.py and video_editor.py
    scraper_thread = threading.Thread(target=run_twitch_scraper)
    editor_thread = threading.Thread(target=run_video_editor)

    # Start the threads for twitch_scraper.py and video_editor.py
    scraper_thread.start()
    scraper_thread.join()  # Wait for twitch_scraper.py to finish before starting video_editor.py
    editor_thread.start()
    editor_thread.join()  # Wait for video_editor.py to finish before starting the next two functions

    # Create thread for running youtube_uploader.py
    uploader_thread = threading.Thread(target=run_youtube_uploader)

    # Start the thread for youtube_uploader.py
    uploader_thread.start()