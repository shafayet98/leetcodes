
from collections import defaultdict
strs = ["act","pots","tops","cat","stop","hat"]

def anagramGroup(strs):
    d = defaultdict(list)
    for itm in strs:
        sorter_itm = ''.join(sorted(itm))
        d[sorter_itm].append(itm)

    res = list(d.values())
    return res

print(anagramGroup(strs))