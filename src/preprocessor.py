import re

STOP_WORDS = {"a", "an", "the", "is", "am", "are", "was", "were", "be", "been", "being", "in", "on", "at", "to", "for",
            "of", "and", "or", "but", "this", "that", "these", "those", "it", "its", "as", "by", "from", "with", "about" }


def split_into_sentences(text):
    """Split text into individual sentences."""

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    return [sentence for sentence in sentences if sentence]


def extract_words(sentence):
    """Extract meaningful, normalized words from a sentence."""

    words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())

    meaningful_words = [word for word in words if word not in STOP_WORDS ]

    return meaningful_words
