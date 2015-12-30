import re

fh = open('inp.txt')

for line in fh:
    print re.findall('.+@(.+)',line)[0]
