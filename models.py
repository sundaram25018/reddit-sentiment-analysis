from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Example model for sentiment analysis result
class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    sentiment = Column(String)
    polarity = Column(Float)

