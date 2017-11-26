from functools import reduce
from operator import itemgetter

a_list = ['100', '10', '1']
sorted_li = sorted(a_list, key=len, reverse=True)
sorted_li.sort(key=int)
print(reduce(lambda x, y: x + y, sorted_li))
