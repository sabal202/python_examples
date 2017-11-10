def checkio(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[(len(data) - 1) // 2] + data[(len(data) - 1) // 2 + 1]) / 2
    else:
        return data[(len(data) - 1) // 2]
