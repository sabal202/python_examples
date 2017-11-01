import string

N, K = map(int, input().split())
in_line = input()
print(in_line + max(string.ascii_lowercase, key=in_line.count) * K)
