# Python Regex pracitce

import re

text_to_search = '''abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabc1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
1235551234
800-555-1234
900-555-1234
5555
Mr. Schafer
Mr Smith Mr. Stuart
Ms Davis Mr. Adam
Mrs. Robinson
Mr. T
cat
bat
aab
mat
pat
'''

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

for match in matches:
    print match.group()
    #print match.start(), match.end()
