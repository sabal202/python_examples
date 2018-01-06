import sys, codecs

save_stdin = sys.stdin
save_stdout = sys.stdout
sys.stdin = codecs.open("input.txt", "r", "utf-8")
sys.stdout = codecs.open("output.txt", "w+")


# checks right brackets sequences, if it is not, returns place of error
def is_balanced(line):
    opener = ("[", "{", "(", "<", '"', "'")
    closer = ("]", "}", ")", ">", '"', "'")
    b = 1
    stack = []
    for br in line:
        if br in opener:
            stack.append((br, b))
        elif br in closer:
            if not stack:
                return False, b
            if stack[-1][0] != opener[closer.index(br)]:
                return False, b
            else:
                stack.pop()
        b += 1
    size = len(stack)
    if size:
        return False, stack[-1][1]
    else:
        return True, b


line = input()

a, b = is_balanced(line)
if a:
    print("Right")
else:
    print(b)
