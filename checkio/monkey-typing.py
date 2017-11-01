import re


def count_words(text, words):
    c = 0
    text = text.lower()
    for i in words:
        if re.search(i.lower(), text):
            c += 1
    return c
