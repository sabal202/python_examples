def non_repeat(line):
    n = len(line)
    l = [-1] * 256
    i = 0
    ss = [""]
    for j in range(n):
        i = max(l[ord(line[j])], i)
        l[ord(line[j])] = j + 1
        ss.append(line[i:j + 1])

    return max(ss, key=len)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
