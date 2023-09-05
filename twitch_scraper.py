import requests
import youtube_dl
import datetime
import re

# Get the current date and time
now = datetime.datetime.now()

# Calculate the start and end date for yesterday
yesterday = now - datetime.timedelta(days=1)
start_date = yesterday.replace(hour=0, minute=0, second=0).strftime("%Y-%m-%dT%H:%M:%SZ")
end_date = yesterday.replace(hour=23, minute=59, second=59).strftime("%Y-%m-%dT%H:%M:%SZ")

def clean_title(title):
    # Remove non-alphanumeric characters from the title
    cleaned_title = re.sub(r'\W+', ' ', title)
    return cleaned_title

def scrape_twitch_clips():
    # Define the access token and client ID
    access_token = ""
    client_id = ""
    
    # Define the headers with the access token and client ID
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-ID": client_id
    }
    
    # Define the list of broadcaster IDs for the streamers
    broadcaster_ids = ["", "", "", "", "", "", "", "", "", "", ""]

    # Iterate over the broadcaster IDs and retrieve clips for each streamer
    for broadcaster_id in broadcaster_ids:
        # Send a GET request to the Twitch API to retrieve the clips for the current streamer
        response = requests.get(f"https://api.twitch.tv/helix/clips?broadcaster_id={broadcaster_id}&first=4&started_at={start_date}&ended_at={end_date}", 
                                headers=headers)
        
        if response.status_code == 200:
            # Process the response and extract relevant information
            clips_data = response.json()
            clips = clips_data["data"]
            
            # Process the clips data and extract relevant information
            for clip in clips:
                clip_title = clip["title"]
                clip_url = clip["url"]
                clip_views = clip["view_count"]
                
                # Clean the clip title to remove non-alphanumeric characters
                cleaned_title = clean_title(clip_title)
                
                # Download the clip
                output_path = f"{cleaned_title}.mp4"
                
                ydl_opts = {
                    'outtmpl': output_path,
                }
                
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([clip_url])
                    
                print(f"Clip downloaded successfully for broadcaster ID: {broadcaster_id}")
        
        else:
            print("Failed to retrieve Twitch clips for broadcaster ID:", broadcaster_id, "Status code:", response.status_code)

# Call the function to start scraping Twitch clips
scrape_twitch_clips()