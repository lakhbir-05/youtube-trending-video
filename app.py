import streamlit as st
import pandas as pd
import numpy as np
import joblib
from googleapiclient.discovery import build

# Your API Key
API_KEY = "AIzaSyCanSmcA8wrmJIIa2SzAeSKkLKTwEuhRdI"
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Load model and data
model = joblib.load("trending_model.pkl")
scaler = joblib.load("scaler.pkl")
df = joblib.load("youtube_data.pkl")

st.title("📺 YouTube Trending Video Predictor & Topic Search")

# --- Prediction Section ---
st.header("🎯 Predict if Your Video Will Trend")

# User input for video features
likes = st.number_input("Likes", min_value=0)
dislikes = st.number_input("Dislikes", min_value=0)
comments = st.number_input("Comment Count", min_value=0)
category = st.number_input("Category ID", min_value=1)
publish_hour = st.number_input("Publish Hour (0-23)", min_value=0, max_value=23)
publish_day = st.number_input("Publish Day (1-31)", min_value=1, max_value=31)
publish_month = st.number_input("Publish Month (1-12)", min_value=1, max_value=12)
tag_count = st.number_input("Tag Count", min_value=0)

if st.button("Predict Trending"):
    input_data = np.array([[likes, dislikes, comments, category, publish_hour, publish_day, publish_month, tag_count]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    st.success("This video is likely to TREND!" if prediction[0] == 1 else "This video is NOT likely to trend.")



# --- Topic Search Section ---
st.header("🔍 Search Videos by Topic (Live from YouTube)")

topic = st.text_input("Enter a topic (e.g., Cricket, Bollywood):")

if topic:
    request = youtube.search().list(
        q=topic,
        part="snippet",
        type="video",
        maxResults=5
    )
    response = request.execute()

    if len(response['items']) == 0:
        st.warning("No videos found for this topic.")
    else:
        st.write("### Videos Found (Live):")
        for item in response['items']:
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            thumbnail = item['snippet']['thumbnails']['medium']['url']
            youtube_link = f"https://www.youtube.com/watch?v={video_id}"
            st.write(f"**{title}**")
            st.markdown(f"[![Watch Here]({thumbnail})]({youtube_link})")


