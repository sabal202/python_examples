import textwrap

sample_text = '''
        The textwrap module can be used to format text for output in situations
        where pretty-printing is desired.  It offers programmatic functionality similar
        to the paragraph wrapping or filling features found in many text editors.
        '''

# Remove any common leading whitespace from every line in text.
print(textwrap.dedent(sample_text).strip())
# The textwrap module can be used to format text for output in situations
# where pretty-printing is desired.  It offers programmatic functionality similar
# to the paragraph wrapping or filling features found in many text editors.

# Input like
#
# ␣Line one.
# ␣␣␣Line two.
# ␣Line three.

# becomes
#
# Line one.
# ␣␣Line two.
# Line three.


# The results are something less than desirable.
# The text is now left justified, but the first line retains its indent
# and the spaces from the front of each subsequent line are embedded in the paragraph.
print(textwrap.fill(sample_text, width=50))
#      The textwrap module can be used to format
# text for output in     situations where pretty-
# printing is desired.  It offers     programmatic
# functionality similar to the paragraph wrapping
# or filling features found in many text editors.

# function to add consistent prefix text to all of the lines in a string.
dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')


#
# >  The textwrap module can be used to format text
# > for output in situations where pretty-printing is
# > desired.  It offers programmatic functionality
# > similar to the paragraph wrapping or filling
# > features found in many text editors.
#
# > Second paragraph after a blank line.

def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN ', predicate=should_indent)

print('\nQuoted block:\n')
print(final)

# Indent ' The textwrap module can be used to format text\n'?
# Indent 'for output in situations where pretty-printing is\n'?
# Indent 'desired.  It offers programmatic functionality\n'?
# Indent 'similar to the paragraph wrapping or filling\n'?
# Indent 'features found in many text editors.'?
#
# Quoted block:
#
# EVEN  The textwrap module can be used to format text
# for output in situations where pretty-printing is
# EVEN desired.  It offers programmatic functionality
# EVEN similar to the paragraph wrapping or filling
# EVEN features found in many text editors.


# To truncate text to create a summary or preview, use shorten().
print(textwrap.shorten(sample_text, 100))
# The textwrap module can be used to format text for output in situations where pretty-printing [...]


# This makes it possible to produce a hanging indent, where the first line is indented less than the other lines.
dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50,
                    ))

# The textwrap module can be used to format text for
#     output in situations where pretty-printing is
#     desired.  It offers programmatic functionality
#     similar to the paragraph wrapping or filling
#     features found in many text editors.
