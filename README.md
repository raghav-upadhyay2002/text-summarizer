=============================
TEXT SUMMARIZER
=============================

A simple AI-powered text summarization app built with Hugging Face Transformers 
and Streamlit. You can paste any article or blog text, and the app will generate 
a concise summary.

This project was created as part of an AI mini-assignment to demonstrate effort, 
resourcefulness, and creativity.

-----------------------------
FEATURES
-----------------------------
- Summarize long text into a short, readable version
- Adjustable minimum and maximum summary length (sliders in UI)
- Reusable summarizer logic (summarizer.py) for both notebook and app
- Clean Streamlit web interface
- Jupyter notebook (summary_text.ipynb) for experiments
- Model: sshleifer/distilbart-cnn-12-6

-----------------------------
PROJECT STRUCTURE
-----------------------------
text-summarizer/
├─ app.py                 # Streamlit app
├─ summarizer.py          # Core summarizer functions
├─ summary_text.ipynb     # Jupyter notebook experiments
├─ requirements.txt       # Dependencies
├─ README.txt             # Project documentation
└─ .gitignore

-----------------------------
SETUP INSTRUCTIONS
-----------------------------
1. Clone the Repository:
   git clone https://github.com/raghav-upadhyay2002/text-summarizer.git
   cd text-summarizer

2. Install Dependencies:
   pip install -r requirements.txt

3. Run the Streamlit App:
   streamlit run app.py

   → Open the link in your browser (usually http://localhost:8501)

-----------------------------
USAGE
-----------------------------
1. Paste an article or blog text into the text box
2. Adjust min and max summary length using the sliders
3. Click "Summarize"
4. The summary will appear below

-----------------------------
USING THE NOTEBOOK
-----------------------------
You can also test the summarizer directly in summary_text.ipynb:

from summarizer import summarize_text, load_summarizer
load_summarizer()
text = """Your article here..."""
summary = summarize_text(text, min_length=40, max_length=120)
print(summary)

-----------------------------
STRETCH GOALS
-----------------------------
- Add URL input to fetch and summarize online articles
- Add "Download Summary" button
- Deploy the app on Hugging Face Spaces or Render

-----------------------------
ACKNOWLEDGEMENTS
-----------------------------
- Hugging Face Transformers
- Streamlit
- GPT (used for debugging and guidance during development)