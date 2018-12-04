"""
DNA find all matching items from a list in a string (python 2.7)

INPUT:

  data_1 = "ATGCTGCATGTCATGTGCTGATCTG"
  wild_type = ["A", "TG", "ATGC", "ATG", "TGCT", "GTA", "GTACT", "GT", "CT"]

I want the output to be a list of indexes in data_1 where matches from wild_type were found.

Additionally, I want to find the longest piece that matches. So for the first part of the string, A, ATG, ATGC all match,
so I don't need it to spit out [0,1,2,3], but rather just [0,3] (a range)

"""

import re
from operator import sub


def match(wild_type, data_1):
    d = {}
    import ipdb; ipdb.set_trace()
    for i in wild_type:
        match = re.search('{}'.format(i),data_1)
        if match:
            i,j = match.span()
            d.setdefault(i,[]).append(j)
    return max(((i,j[-1]) for i,j in d.items()),key=lambda x:abs(sub(*x)))

if __name__ == "__main__":
    data_1 = "ATGCTGCATGTCATGTGCTGATCTG"
    wild_type = ["A", "TG", "ATGC", "ATG", "TGCT", "GTA", "GTACT", "GT", "CT"]
    print match(wild_type, data_1)
