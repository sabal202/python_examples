def checkio(matrix):
    N = len(matrix)
    # Horizontal
    for i in range(N):
        for j in range(N - 3):
            last = matrix[i][j]
            c = 1
            for k in range(j + 1, N):
                if matrix[i][k] == last:
                    c += 1
                else:
                    break
                last = matrix[i][k]
                if c == 4:
                    return True

    # Vertical
    for i in range(N - 3):
        for j in range(N):
            last = matrix[i][j]
            c = 1
            for k in range(i + 1, N):
                if matrix[k][j] == last:
                    c += 1
                else:
                    break
                last = matrix[k][j]
                if c == 4:
                    return True

    # Diagonal right-down
    for i in range(N - 3):
        for j in range(N - 3):
            last = matrix[i][j]
            c = 1
            d = i
            for k in range(j + 1, N):
                d += 1
                if matrix[d][k] == last:
                    c += 1
                else:
                    break
                last = matrix[d][k]

                if c == 4:
                    return True

    # Diagonal right-up
    for i in range(3, N):
        for j in range(N - 3):
            last = matrix[i][j]
            c = 1
            d = i
            for k in range(j + 1, N):
                d -= 1
                if matrix[d][k] == last:
                    c += 1
                else:
                    break
                last = matrix[d][k]

                if c == 4:
                    return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
