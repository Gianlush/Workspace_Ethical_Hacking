with open('fluff', 'rb') as f:
  s = f.read()

for i in b'flag.txt':
  print(f"{chr(i)} -> {hex(s.find(i))}")
