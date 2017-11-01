def long_repeat(line):
    grouped_list = []
    temp_list = []
    for i in range(len(line)):
        if len(temp_list) == 0:
            temp_list.append(line[i])
        if i != len(line) - 1:
            if line[i][0] == line[i + 1][0]:
                temp_list.append(line[i + 1])
            else:
                grouped_list.append(temp_list)
                temp_list = []
                temp_list.append(line[i + 1])
                continue
    grouped_list.append(temp_list)
    return max([len(i) for i in grouped_list])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
