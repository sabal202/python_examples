import re

s = input()
s = re.compile('[^a-zA-Z]').sub("", s)
print(s)
