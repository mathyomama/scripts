def problem100(limit = 10**12):
   pv, v = 1, 4
   while v < limit: pv, v = v, v*6 - pv - 2
   return int(v * (.5 ** .5)) + 1

print(problem100())
