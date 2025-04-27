from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import praw
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Reddit API client setup
reddit = praw.Reddit(client_id="kStoVfPXD1ExOTku7AE04w",
                     client_secret="p6zfLflDLjEABBN9RMQIU2W9JMH9FQ",
                     user_agent="sentiment_analysis_app by/u/Available-Humor-2860")

# Define the Pydantic models
class Subreddit(BaseModel):
    name: str
    limit: int = 10
    time_filter: str = "day"
    analysis_type: str = "sentiment"  # Default to sentiment analysis

# Output Schema
class SentimentResult(BaseModel):
    title: str
    emotion: str = "neutral"  # Default to neutral for emotion
    sentiment: str = "neutral"  # Default to neutral for sentiment
    polarity: float
    author: str
    created_utc: float
    url: str
    score: int
    num_comments: int
    subreddit: str

@app.post("/analyze_sentiment", response_model=List[SentimentResult])
def analyze_sentiment(subreddit: Subreddit):
    try:
        subreddit_name = subreddit.name.replace(" ", "").lower()
        posts = reddit.subreddit(subreddit_name).top(time_filter=subreddit.time_filter, limit=subreddit.limit)

        sentiment_results = []
        analyzer = SentimentIntensityAnalyzer()

        for post in posts:
            analysis = TextBlob(post.title)
            polarity = analysis.sentiment.polarity
            sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
            
            # Use sentiment analysis or emotion detection based on the radio button choice
            if subreddit.analysis_type == "sentiment":
                sentiment_results.append(SentimentResult(
                    title=post.title,
                    sentiment=sentiment,
                    polarity=polarity,
                    emotion="neutral",  # No emotion for sentiment analysis
                    author=str(post.author),
                    created_utc=post.created_utc,
                    url=post.url,
                    score=post.score,
                    num_comments=post.num_comments,
                    subreddit=post.subreddit.display_name,
                ))
            elif subreddit.analysis_type == "emotion":
                # Use VADER for emotion detection
                sentiment_scores = analyzer.polarity_scores(post.title)
                emotion = 'neutral'  # Default to neutral
                if sentiment_scores['compound'] >= 0.05:
                    emotion = 'positive'
                elif sentiment_scores['compound'] <= -0.05:
                    emotion = 'negative'
                
                sentiment_results.append(SentimentResult(
                    title=post.title,
                    emotion=emotion,
                    sentiment="neutral",  # No sentiment for emotion detection
                    polarity=sentiment_scores['compound'],
                    author=str(post.author),
                    created_utc=post.created_utc,
                    url=post.url,
                    score=post.score,
                    num_comments=post.num_comments,
                    subreddit=post.subreddit.display_name,
                ))

        return sentiment_results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
