# import Python_pkg.pkg
import tracemalloc
import sys
import collections
from collections import defaultdict
from Python_pkg import pkg

pkg.say()
# print(r)

s = 'wertyjkmrthyjguhkmngfeagesthgr'
d = {}
for value in s:
    if value not in d:
        d[value] = 0
    d[value] += 1
print(d)

f = {}
for c in s:
    f.setdefault(c, 0)
    f[c] += 1
print(f)

f = defaultdict(int)
for c in s:
    f[c] += 1
print(f)

print(f['f'])


print(sys.path)
