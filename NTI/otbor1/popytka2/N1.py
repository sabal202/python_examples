# TAGS:
import re

s = input()
if re.match(r"[A-Z][0-9]{3}[A-Z]{2}", s):
    print("Yes")
else:
    print("No")