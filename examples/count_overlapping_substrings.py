def count_overlapping_substrings(haystack, needle):
    count = 0
    i = -1
    while True:
        i = haystack.find(needle, i + 1)
        if i == -1:
            return count
        count += 1
