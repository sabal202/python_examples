def non_repeat(line):
    n = len(line)
    length = 0
    l = [-1] * 256
    i = 0
    ss = [""]
    for j in range(n):
        i = max(l[ord(line[j])], i)
        length = max(length, j - i + 1)
        l[ord(line[j])] = j + 1
        ss.append(line[i:j + 1])

    return max(ss, key=len), length
