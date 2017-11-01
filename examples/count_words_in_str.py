def count_words(text, words):
    return sum(w in text.lower() for w in words)


if __name__ == '__main__':
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
