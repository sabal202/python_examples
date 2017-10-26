import string

"""
We iterate through latyn alphabet and count each letter in the text.
Then 'max' selects the most frequent letter.
For the case when we have several equal letter,
'max' selects the first from they.
"""
text = input().lower()
print(max(string.ascii_lowercase, key=text.count))
