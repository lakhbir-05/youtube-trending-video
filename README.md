# youtube-trending-video
trending video predictor
📺 YouTube Trending Video Predictor & Topic Search
📌 Project Overview

This project predicts whether a YouTube video will trend or not using Machine Learning techniques. It also provides a feature to search live videos based on a topic using the YouTube API. The system is built using Python, Scikit-learn, and Streamlit for an interactive user interface.

🚀 Features
Predicts if a video will trend based on input features
Uses Random Forest Machine Learning model
Performs data preprocessing and feature engineering
Hyperparameter tuning using GridSearchCV and Optuna
Interactive Streamlit web application
Live video search using YouTube API
🛠️ Technologies Used
Python
Pandas, NumPy
Seaborn, Matplotlib
Scikit-learn
Optuna
Streamlit
YouTube Data API
📂 Dataset
Dataset used: Indian YouTube Trending Dataset (INvideos.csv)
Contains features like views, likes, dislikes, comments, category, and publish time
⚙️ How It Works
Load and preprocess the dataset
Perform feature engineering
Train Random Forest model
Tune model using GridSearchCV and Optuna
Save model and scaler
Deploy using Streamlit
Take user input and predict results
📊 Input Features
Likes
Dislikes
Comment Count
Category ID
Publish Hour, Day, Month
Tag Count
🎯 Output
Predicts: Trending (1) / Not Trending (0)
Displays live videos based on user topic
▶️ How to Run the Project
Clone the repository
git clone https://github.com/your-username/your-repo-name.git
Install dependencies
pip install -r requirements.txt
Run Streamlit app
streamlit run app.py
📌 Future Enhancements
Use advanced models like XGBoost or Deep Learning
Add more features like title sentiment and thumbnails
Deploy the app online
Use real-time streaming data
👩‍💻 Author
LAKHBIR KAUR
🔗 Live Application

👉 Click here to use the app: https://youtube-trending-video-gpgkrth677xtirutggze37.streamlit.app/
