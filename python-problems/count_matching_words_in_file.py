import re
import collections

wanted = ["angularjs", "services"]
matches = re.findall('\w+',open('angularjs.txt').read().lower())
counts = collections.Counter(matches) # Count each occurance of words
map(lambda x:(x,counts[x]),wanted) # Will print the counts for wanted words
