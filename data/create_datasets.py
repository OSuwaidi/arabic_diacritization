from util import clean_arabic, tokenize
from rich import print

with open("arabic_sample.txt", "r", encoding="utf8") as file:
    first_lines = []
    for i in range(20):
        first_lines.append(clean_arabic(file.readline()))
    print(tokenize("\n".join(first_lines)))
