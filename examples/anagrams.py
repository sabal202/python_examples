def anagrams(word, words):
    import string
    w = [word.count(i) for i in string.ascii_letters]
    return [wordi for wordi in words if w == [wordi.count(i) for i in string.ascii_letters]]
