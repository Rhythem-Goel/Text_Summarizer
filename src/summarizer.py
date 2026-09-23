from src.scorer import (
    calculate_word_frequencies,
    calculate_sentence_score
)


def generate_summary(sentences, summary_length):
    """Generate a summary containing the highest-scoring sentences."""

    if not sentences:
        return ""

    if summary_length <= 0:
        return ""

    if summary_length >= len(sentences):
        return " ".join(sentences)

    word_frequencies = calculate_word_frequencies(sentences)

    scored_sentences = []

    for index, sentence in enumerate(sentences):
        score = calculate_sentence_score(
            sentence,
            word_frequencies
        )

        scored_sentences.append((index, sentence, score))

    # Select the highest-scoring sentences.
    ranked_sentences = sorted(
        scored_sentences,
        key=lambda item: item[2],
        reverse=True
    )

    selected = ranked_sentences[:summary_length]

    # Restore the original order of the selected sentences.
    selected.sort(key=lambda item: item[0])

    return " ".join(sentence for _, sentence, _ in selected)