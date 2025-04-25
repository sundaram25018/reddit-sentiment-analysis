# 🧠 Reddit Sentiment Analysis App

This project is a full-stack application that performs **sentiment analysis** on Reddit posts from any subreddit. It uses **FastAPI** for the backend and **Streamlit** for the frontend, allowing users to input a subreddit name, choose the number of posts, and select a time range for analysis.

## 🚀 Features

- 🔍 Input any subreddit to analyze
- 🕐 Choose time filter: `day`, `week`, `month`, `year`, or `all`
- 📦 Select number of posts (5 to 50)
- 🤖 Sentiment analysis with TextBlob (`positive`, `neutral`, `negative`)
- 📊 Beautiful data visualizations:
  - Bar chart of sentiment distribution
  - Pie chart of sentiment ratio
  - Word cloud of post titles
- 📰 Expandable post cards with metadata and links
- 📥 Export results as CSV

---

## 🧩 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **NLP**: TextBlob
- **Reddit API**: PRAW (Python Reddit API Wrapper)
- **Visualization**: Matplotlib, Seaborn, WordCloud

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/reddit-sentiment-app.git
cd reddit-sentiment-app
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Configure Reddit API Credentials
Edit the main.py and replace:
```bash
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="sentiment_analysis_app"
)
```

🔐 Create a Reddit app at https://www.reddit.com/prefs/apps

### 🧪 Run the Application
# Start FastAPI Backend
```bash
uvicorn main:app --reload
```
## Start Streamlit Frontend
```bash
streamlit run app.py
```
# 📸 Screenshots
![image](https://github.com/user-attachments/assets/ee532f66-6427-4ed8-b0ea-df1af28ffc3f)
![image](https://github.com/user-attachments/assets/8fab191b-ce18-4a21-a480-e21345288206)
![image](https://github.com/user-attachments/assets/b46cb847-5c89-4a86-baa5-25c745756dff)
![image](https://github.com/user-attachments/assets/70f81c9a-c27f-4886-bdde-3b1c9a3866c8)



### 🧠 Future Ideas
- 🔎 Filter posts by keyword
- 💬 Analyze top-level comments
- 📈 Sentiment trend over time
- 🧠 Use a more advanced sentiment model (e.g., BERT)

# 📄 License
MIT License © 2025 Sundaram Dubey
