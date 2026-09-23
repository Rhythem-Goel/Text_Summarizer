import tempfile
from pathlib import Path
from src.preprocessor import split_into_sentences, extract_words
from src.scorer import (
    calculate_word_frequencies,
    calculate_sentence_score
)
from src.summarizer import generate_summary
from src.reader import read_text_file

def test_split_into_sentences():
    text = "Python is easy. Python is powerful!"
    
    sentences = split_into_sentences(text)

    assert len(sentences) == 2
    assert sentences[0] == "Python is easy."
    assert sentences[1] == "Python is powerful!"


def test_extract_words():
    sentence = "Python is easy to learn."

    words = extract_words(sentence)

    assert words == ["python", "easy", "learn"]

def test_calculate_word_frequencies():
    sentences = [
        "Python is powerful.",
        "Python is easy to learn."
    ]

    frequencies = calculate_word_frequencies(sentences)

    assert frequencies["python"] == 2
    assert frequencies["powerful"] == 1
    assert frequencies["easy"] == 1


def test_calculate_sentence_score():
    sentences = [
        "Python is powerful.",
        "Python is easy to learn."
    ]

    frequencies = calculate_word_frequencies(sentences)

    score = calculate_sentence_score(
        sentences[0],
        frequencies
    )

    assert score > 0

def test_generate_summary_preserves_order():
    sentences = [
        "Python is popular.",
        "The weather is pleasant.",
        "Python is powerful.",
        "The sky is blue."
    ]

    summary = generate_summary(sentences, 2)

    selected_indices = [
        i for i, sentence in enumerate(sentences)
        if sentence in summary
    ]

    assert selected_indices == sorted(selected_indices)

def test_empty_summary():
    assert generate_summary([], 2) == ""


def test_zero_length_summary():
    sentences = ["Python is useful."]

    assert generate_summary(sentences, 0) == ""


def test_read_text_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "test.txt"

        file_path.write_text(
            "Python is powerful.",
            encoding="utf-8"
        )

        text = read_text_file(file_path)

        assert text == "Python is powerful."

def test_missing_file():
    try:
        read_text_file("does_not_exist.txt")
        assert False
    except FileNotFoundError:
        assert True

if __name__ == "__main__":
    test_split_into_sentences()
    test_extract_words()
    test_calculate_word_frequencies()
    test_calculate_sentence_score()
    test_generate_summary_preserves_order()
    test_empty_summary()
    test_zero_length_summary()
    test_read_text_file()
    print("All tests passed!")