"""
I have the following lists in Python:

INPUT:
    students = ["Anderson", "Peter", "Anderson", "Bastian"]
    courses = ["Biology", "History", "Maths", "History"]
I have coded a for loop in an attempt to relate these pairs in a dictionary, so that:

{'Peter': ['History'], 'Anderson': ['Biology', 'Maths'], 'Bastian': ['History']}

"""

"Python dictionaries doesn't accepts duplicate keys and in your code"

def merge_list_to_dict(students, courses):
    d = {}
    for i,j in zip(students,courses):
        d.setdefault(i,[]).append(j)
    return d

if __name__ == '__main__':
    students = ["Anderson", "Peter", "Anderson", "Bastian"]
    courses = ["Biology", "History", "Maths", "History"]
    print merge_list_to_dict(students, courses)
