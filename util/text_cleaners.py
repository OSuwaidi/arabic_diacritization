import re

_whitespace_re = re.compile(r"\s+")


def collapse_whitespace(text):
    text = re.sub(_whitespace_re, " ", text)
    return text


def basic_cleaners(text):
    text = collapse_whitespace(text)
    return text.strip()


arabic_pattern = re.compile(r"[\u0600-\u06FF\u0610-\u061A\u064B-\u065F\s]+")
# [\u0600-\u06FF]: Matches Arabic letters and symbols.
# [\u0610-\u061A\u064B-\u065F]: Matches Arabic diacritics.
# \s: Matches any whitespace characters (spaces, tabs, newlines, etc.).
def clean_arabic(text):
    matches = arabic_pattern.findall(collapse_whitespace(text))
    # Join the matches to form the final string with only Arabic characters and diacritics
    return ''.join(matches).strip()

def tokenize(text: str):
    tokens = text.split()
    return [token for token in tokens if len(token) > 1]
