d = {}

s = "abcab"

d.item

for i, c in enumerate(s):
    if not c in d:
        d[c] = []
    d[c].append(i)

for k in d:
  if len(d[k]) == 1:
      print(d[k].pop())
