from collections import Counter

file = open("angular.txt", "r")

num_char = 0
num_words = 0
num_lines = 0
char_distribution = Counter()

for line in file:
    words = line.split()
    num_lines += 1
    num_words += len(words)
    num_char += len(line)
    char_distribution += Counter(line.lower())

print("Character count:\t{}".format(num_char))
print("Word count:\t\t{}".format(num_words))
print("Line count:\t\t{}".format(num_lines))
print("Distribution of characters: ")
for char, count in sorted(char_distribution.items()):
    if char.isalpha() or char in ',.':
        print("\t{}\t\t{}".format(char, count))