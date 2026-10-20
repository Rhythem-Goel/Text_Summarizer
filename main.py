from pathlib import Path

from src.reader import read_text_file
from src.preprocessor import split_into_sentences
from src.summarizer import generate_summary


PROJECT_ROOT = Path(__file__).resolve().parent

INPUT_FILE = PROJECT_ROOT / "data" / "input.txt"
OUTPUT_FILE = PROJECT_ROOT / "output" / "summary.txt"

def main():
    """Run the text summarizer application."""

    try:
        text = read_text_file(INPUT_FILE)

        sentences = split_into_sentences(text)

        if not sentences:
            print("The input file does not contain any sentences.")
            return

        print("=" * 40)
        print("        TEXT SUMMARIZER")
        print("=" * 40)

        print(f"\nInput file: {INPUT_FILE}")
        print(f"Total sentences: {len(sentences)}")

        summary_length = int(input("Enter number of sentences for summary: "))

        if summary_length <= 0:
            print("Summary length must be greater than zero.")
            return

        summary = generate_summary(sentences,summary_length)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(summary)

        print("\nSummary:")
        print("-" * 40)
        print(summary)
        print("-" * 40)

        print(f"\nSummary saved to: {OUTPUT_FILE}")

    except ValueError:
        print("Please enter a valid integer.")

    except FileNotFoundError as error:
        print(error)

    except PermissionError as error:
        print(error)

    except OSError as error:
        print(f"File error: {error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()