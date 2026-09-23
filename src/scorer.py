from collections import Counter

from src.preprocessor import extract_words


def calculate_word_frequencies(sentences):
    """Calculate the frequency of meaningful words in the text."""

    all_words = []

    for sentence in sentences:
        words = extract_words(sentence)
        all_words.extend(words)

    return Counter(all_words)


def calculate_sentence_score(sentence, word_frequencies):
    """Calculate an importance score for a sentence."""

    words = extract_words(sentence)

    if not words:
        return 0.0

    score = sum(word_frequencies[word] for word in words)

    return score / len(words)