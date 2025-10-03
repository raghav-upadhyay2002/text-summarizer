# summarizer.py
from transformers import pipeline
_summarizer = None

def load_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )
    return _summarizer

def summarize_text(text: str, min_length: int = 40, max_length: int = 120) -> str:
    summarizer = load_summarizer()
    # Simple guardrails
    min_length = max(5, min_length)
    max_length = max(min_length + 5, max_length)

    # (Optional) short chunking to avoid overly long inputs
    if len(text) > 4000:
        text = text[:4000]

    out = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
    return out[0]["summary_text"]
