import re
pattern = re.compile(r"([a-zA-Z0-9$%#@]{8,}\d)")
string = 'searchingin8l'
a = pattern.fullmatch(string)
print(a)