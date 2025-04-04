import streamlit as st
import json
import datetime
from streamlit.components.v1 import html

# Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
        .comment-box {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border: 1px solid #e0e0e0;
        }
        .comment-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }
        .comment-header h4 {
            color: #2c3e50;
            font-weight: 600;
        }
        .comment-time {
            color: #7f8c8d;
            font-size: 0.8rem;
        }
        .emoji-reactions {
            display: flex;
            gap: 0.5rem;
            margin-top: 0.5rem;
        }
        .stTextArea [data-baseweb="textarea"] {
            min-height: 120px;
        }
    </style>
    """, unsafe_allow_html=True)

# Function to load comments from the JSON file
def load_comments():
    try:
        with open("comments.json", "r") as f:
            comments = json.load(f)
    except FileNotFoundError:
        comments = []
    return comments

# Function to save comments to the JSON file
def save_comments(comments):
    with open("comments.json", "w") as f:
        json.dump(comments, f, indent=4)

# Apply custom CSS
local_css()

# Page header
st.title("🌱 Community Garden")
st.markdown("""
Welcome to our community space! Share your thoughts, questions, or gardening tips below.
The most recent comments will appear at the top.
""")
st.divider()

# Load existing comments
comments = load_comments()

# Display existing comments in reverse chronological order
if comments:
    st.subheader("💬 Recent Comments")
    for comment in reversed(comments):
        timestamp_str = comment.get("timestamp", "unknown time")
        with st.container():
            st.markdown(f"""
            <div class="comment-box">
                <div class="comment-header">
                    <h4>👤 {comment['name']}</h4>
                    <span class="comment-time">⏰ {timestamp_str}</span>
                </div>
                <p>{comment['comment']}</p>
                <div class="emoji-reactions">
                    <span>👍</span>
                    <span>❤️</span>
                    <span>😊</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("🌻 No comments yet. Be the first to share your thoughts!")

# User input section
st.divider()
st.subheader("✍️ Share Your Thoughts")

with st.form("comment_form"):
    name = st.text_input("Your Name*", help="How you'd like to be shown in comments")
    comment = st.text_area("Your Comment*", 
                         help="Share your gardening tips, questions, or experiences",
                         max_chars=500)
    char_count = st.empty()
    if comment:
        char_count.caption(f"{len(comment)}/500 characters")
    
    submitted = st.form_submit_button("Post Comment", type="primary")
    if submitted:
        if not name.strip():
            st.error("Please enter your name")
        elif not comment.strip():
            st.error("Please write your comment")
        elif len(comment) > 500:
            st.error("Comment is too long (max 500 characters)")
        else:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_comment = {
                "name": name.strip(),
                "comment": comment.strip(),
                "timestamp": timestamp
            }
            comments.append(new_comment)
            save_comments(comments)
            st.balloons()
            st.success("🎉 Thanks for sharing! Your comment has been posted.")
            st.rerun()
