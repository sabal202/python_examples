# Примеры

# входные данные
# abrakadabrabrakadabra
# выходные данные
# YES
# abrakadabra

# входные данные
# acacacaca
# выходные данные
# YES
# acaca

# Примечание
# Во втором примере подходящим ответом также является строка acacaca.

# входные данные
# abcabc
# выходные данные
# NO

# входные данные
# abababab
# выходные данные
# YES
# ababab

# входные данные
# tatbt
# выходные данные
# NO
import re

msg = input()
str = "-1"

for i in range(1, int(len(msg) / 2 + 1)):
    m = re.match(msg[i:], msg)
    if m is not None:
        str = m.group(0)
        break
if str == "-1":
    print("NO")
elif len(re.findall(str, msg)) > 1:
    print("NO")
else:
    print("YES")
    print(str)
