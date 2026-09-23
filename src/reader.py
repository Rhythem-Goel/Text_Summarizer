def read_text_file(file_path):
    """Read and return the contents of a text file."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {file_path}")

    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")

    except OSError as error:
        raise OSError(f"Could not read file: {error}")