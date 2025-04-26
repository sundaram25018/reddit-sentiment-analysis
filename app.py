import streamlit as st
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns

st.set_page_config(page_title="Reddit Sentiment Analyzer", layout="wide")
st.title("📈 Reddit Sentiment Analysis App")
st.caption("Enter a subreddit name (e.g., 'AskReddit', 'technology', 'news') to analyze sentiment trends from top posts.")

# Sidebar input
with st.sidebar:
    st.header("🔍 Search Subreddit")
    subreddit_name = st.text_input("Subreddit Name", "")
    num_posts = st.slider("Number of Posts", min_value=5, max_value=50, value=10)
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit + FastAPI")

time_filter = st.selectbox(
    "Select Time Range",
    options=["day", "week", "month", "year", "all"],
    index=0  # Default is "day"
)

if subreddit_name:
    try:
        response = requests.post("http://localhost:8000/analyze_sentiment",json={"name": subreddit_name, "limit": num_posts,"time_filter": time_filter}
)

        if response.status_code == 200:
            data = response.json()
            sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
            titles = []

            st.subheader("📰 Post Details")
            for result in data:
                sentiment_counts[result['sentiment']] += 1
                titles.append(result['title'])

                with st.expander(result['title']):
                    st.write(f"**Sentiment:** {result['sentiment']} | **Polarity:** {result['polarity']:.2f}")
                    st.write(f"**Author:** {result['author']}")
                    st.write(f"**Score:** {result['score']} | 💬 Comments: {result['num_comments']}")
                    st.write(f"**Posted At:** {pd.to_datetime(result['created_utc'], unit='s')}")
                    st.markdown(f"🔗 [Link to Post]({result['url']})")
                    if result['selftext']:
                        st.markdown("---")
                        st.write(result['selftext'])

            # Sentiment Bar Chart
            st.subheader("📊 Sentiment Distribution")
            fig, ax = plt.subplots()
            sns.barplot(x=list(sentiment_counts.keys()), y=list(sentiment_counts.values()), palette="viridis", ax=ax)
            ax.set_xlabel("Sentiment")
            ax.set_ylabel("Number of Posts")
            st.pyplot(fig)

            # Pie Chart
            st.subheader("🧁 Sentiment Proportion Pie Chart")
            fig_pie, ax_pie = plt.subplots()
            ax_pie.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'lightcoral', 'lightgrey'])
            ax_pie.axis("equal")
            st.pyplot(fig_pie)

            # Word Cloud
            st.subheader("☁️ Word Cloud of Post Titles")
            titles_text = " ".join(titles)
            if titles_text.strip():
                wc = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
                fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
                ax_wc.imshow(wc, interpolation="bilinear")
                ax_wc.axis("off")
                st.pyplot(fig_wc)
            else:
                st.warning("No titles available to generate word cloud.")

            # Download results
            st.subheader("📥 Export Sentiment Data")
            df = pd.DataFrame(data)
            st.download_button(
                label="Download Sentiment Data as CSV",
                data=df.to_csv(index=False),
                file_name=f"{subreddit_name}_sentiment.csv",
                mime="text/csv"
            )
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")