OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    return {
        operation == "conjunction": x and y,
        operation == "disjunction": x or y,
        operation == "implication": not x or y,
        operation == "exclusive": not x and y or x and not y,
        operation == "equivalence": (not x or y) and (x or not y)
    }[True]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
