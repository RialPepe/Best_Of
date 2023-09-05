# Best_Of
"Best_Of" is a comprehensive software project that I developed independently to enhance my programming skills in Python. The primary objective of this project was to automate the process of curating and creating highlight videos from the top streamers on Twitch and uploading them to YouTube as a single, engaging video.

Key Components and Workflow:

Twitch Clip Scraper (twitch_scraper.py): The project starts by scraping Twitch for the most viewed clips of selected streamers from the previous day. It leverages the Twitch API to access clip data, including titles, URLs, and view counts. Each clip is then downloaded and cleaned for further processing.

Video Editing and Compilation (video_editor.py): Once the clips are collected, the project uses the MoviePy library to edit, resize, and concatenate them into a single video. The resolution of the clips is standardized to ensure consistency, and the resulting compilation represents the "Best Of" moments from the selected streamers.

YouTube Upload (youtube_uploader.py): After video compilation, the software enables the automatic upload of the video to YouTube. It utilizes Google's YouTube Data API and OAuth 2.0 for secure authentication and authorization. The script allows customization of video titles and descriptions based on the compilation date and content.

Account Selection and Authentication (account_selector.py): For YouTube uploads, the program automates Google account selection and authentication using Selenium. It simulates user interactions, such as selecting the appropriate Google account and providing login credentials.
