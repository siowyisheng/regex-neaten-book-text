import re

with open('agot.txt', 'r') as f:
    raw = f.read()

# remove line break if preceding character is lower case, or A, or I, or a comma or a space.
processed = re.sub(r'([a-z]|A|I|,|\s)\n', r'\1 ', raw)

# double remaining line breaks for nicer formatting.
processed = processed.replace('\n', '\n\n')

with open('f_agot.txt', 'w') as f:
    f.write(processed)