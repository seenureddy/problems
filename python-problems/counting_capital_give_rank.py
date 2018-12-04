"""
Give ranking basing on the Capital Letters.
i) If two Capital Letters occurs it will be on top ranking
ii) Don't capital letters keep at bottom of the tables
iii) If capital letters matches then basing on index give ranking (
lowest index will have highest ranking) 

INPUT:
------
4
Knight
indian
cHager
daReg


OUTPUT:
-------
Knight
cHager
daReg
indian

"""
_input_cnt = int(raw_input())
def rankTeams(_input_cnt):
    ranks_list, count, compare_value, compare_index = [], None, 0, 0
    for name in range(1, _input_cnt + 1):
        name = raw_input().split(" ")
        count = sum(1 for c in str(name) if c.isupper())
        if compare_value < count:
            compare_value = count
            ranks_list.append(name)
        elif compare_value > count:
            compare_value = count
            ranks_list.append(name)
        elif compare_value == count:
            for index, name_string in enumerate(str(name)):
                if name_string.isupper():
                    if compare_index <= index:
                        compare_index = index
                        ranks_list.append(name)
    for name in ranks_list:
        print name[0]
rankTeams(_input_cnt)
