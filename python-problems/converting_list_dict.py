"""
INPUT:
    list = ['Name=Sachin\n', 'country=India\n', 'game=cricket\n']

I want this list in a dictionary with keys as Name, country, game and values as Sachin, India,
cricket as corresponding values
"""
import re

def list_to_dict(lis):
	return dict(re.findall(r'(\w+)=(\w+)',''.join(lis)))

if __name__ == '__main__':
	lis = ['Name=Sachin\n', 'country=India\n', 'game=cricket\n']
	print list_to_dict(lis)