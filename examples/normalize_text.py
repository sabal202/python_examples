# This code can normalize text to ASCII
import unicodedata

data = u'ïnvéntìvé'
normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
print(normal)
