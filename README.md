# ✂️ Text Summarizer

A simple **rule-based, extractive text summarizer** written in Python. It reads a text file, scores each sentence using a set of rules, and picks the most important sentences to form a short summary. No AI or machine learning is used.

## ✨ Features

- Reads the text to summarize from `data/input.txt`
- Splits the text into sentences
- Picks the most important sentences using rule-based scoring
- Lets you choose how many sentences the summary should have
- Prints the summary and saves it to `output/summary.txt`
- Handles common errors (empty file, invalid input, missing file)

## 📂 Project Structure

```
Text_Summarizer/
├── data/
│   └── input.txt        # Text to summarize
├── output/
│   └── summary.txt      # Generated summary
├── src/
│   ├── reader.py        # Reads the input file
│   ├── preprocessor.py  # Splits text into sentences
│   └── summarizer.py    # Scores sentences and builds the summary
├── tests/               # Tests
└── main.py              # Run this file
```

## 🚀 How to Run

1. Make sure you have **Python 3.8+** installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Rhythem-Goel/Text_Summarizer.git
   cd Text_Summarizer
   ```
3. Paste your text into `data/input.txt`.
4. Run the program:
   ```bash
   python main.py
   ```
5. Enter the number of sentences you want in the summary.

The summary will be shown in the terminal and saved in `output/summary.txt`.

## ⚠️ Limitations

- **Extractive only:** it copies existing sentences and cannot rewrite or paraphrase them.
- **No real understanding:** rules look at the text's surface, not its meaning.
- **Fixed input file:** it always reads `data/input.txt`.
- **Manual input:** the summary length is typed in each time you run it.
- **Output is overwritten:** each run replaces `output/summary.txt`.
- **Sentence splitting is basic:** abbreviations like "Dr." or "e.g." may be split incorrectly.

## 👤 Author

Rhythem Goel · [@Rhythem-Goel](https://github.com/Rhythem-Goel)