from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import date, timedelta

def upload_to_youtube(video_file, video_title, video_description):
    # Set up the OAuth 2.0 credentials
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json",
        scopes=scopes
    )
    credentials = flow.run_local_server(port=0)

    # Create the YouTube Data API client
    youtube = build("youtube", "v3", credentials=credentials)

    # Define the video metadata
    request_body = {
        "snippet": {
            "title": video_title,
            "description": video_description,
        },
        "status": {
            "privacyStatus": "public"  # Set the privacy status (public, private, unlisted)
        },
    }

    # Upload the video to YouTube
    media = MediaFileUpload(video_file)
    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    ).execute()

    if "id" in response:
        print("Video uploaded successfully to YouTube! Video ID:", response["id"])
    else:
        print("Failed to upload video to YouTube.")

# Get yesterday's date
yesterday = date.today() - timedelta(days=1)
yesterday_day = yesterday.strftime("%d")
yesterday_month = yesterday.strftime("%B")

# Define the mapping of month names in Spanish
month_names_spanish = {
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre"
}

# Format the day and month in the desired format
formatted_date = f"{yesterday_day} de {month_names_spanish[yesterday_month]}"

# Example usage
video1 = ""  # Specify the path of the video file you want to upload
video2 = "" 
video3 = ""
video_title = f"MEJORES CLIPS TWITCH HISPANO {formatted_date}!!"
video_description = f"Clips con más visualizaciones del día {formatted_date} de los mejores canales de Twitch hispano!"

# Upload video to YouTube
upload_to_youtube(video1, video_title, video_description)
upload_to_youtube(video2, video_title, video_description)
upload_to_youtube(video3, video_title, video_description)