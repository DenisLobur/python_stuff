from pathlib import Path


def count_words(path):
    """Count words in file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"File {path} not found")
        pass
    else:
        words = contents.split()
        len_words = len(words)
        print(f"There are {len_words} in {path}")


path = Path("text_files/programming.txtz")
count_words(path)
