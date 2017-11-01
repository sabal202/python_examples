def safe_pawns(pawns):
    c = 0
    for i in pawns:
        if i[1] != 1:
            bef = str(int(i[1]) - 1)
            if i[0] != "h":
                if chr(ord(i[0]) + 1) + bef in pawns:
                    c += 1
                    continue
            if i[0] != "a":
                if chr(ord(i[0]) - 1) + bef in pawns:
                    c += 1
                    continue
    return c
