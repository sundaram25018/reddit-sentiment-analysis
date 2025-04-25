from pydantic import BaseModel
from typing import List

class Subreddit(BaseModel):
    name: str
    limit: int = 10
    time_filter: str = "day"

# Output Schema
class SentimentResult(BaseModel):
    title: str
    sentiment: str
    polarity: float
    author: str
    created_utc: float
    url: str
    score: int
    num_comments: int
    subreddit: str
    selftext: str
