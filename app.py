import streamlit as st
from summarizer import summarize_text, load_summarizer

st.set_page_config(page_title="📰 Text Summarizer", layout="centered")
st.title("📰 Text Summarizer")

@st.cache_resource(show_spinner=False)
def _cached_loader():
    return load_summarizer()

article = st.text_area("Paste your article here:", height=250, placeholder="Paste any news/blog text…")
col1, col2 = st.columns(2)
with col1:
    min_len = st.slider("Min summary length", 10, 120, 40, step=5)
with col2:
    max_len = st.slider("Max summary length", 30, 200, 120, step=5)

if st.button("Summarize", type="primary"):
    if not article.strip():
        st.warning("Please paste some text first.")
    elif min_len >= max_len:
        st.error("Min length must be smaller than max length.")
    else:
        with st.spinner("Loading model & generating summary…"):
            _ = _cached_loader()  # ensures one-time model init
            summary = summarize_text(article, min_length=min_len, max_length=max_len)
        st.subheader("Summary")
        st.write(summary)

st.caption("Model: sshleifer/distilbart-cnn-12-6 · Hugging Face Transformers")
