def reverse(strs):
    """
    reverse the given string
    """
    return ''.join([strs[i] for i in xrange(len(strs)-1, -1, -1)])

def get_no_of_possible_palindromes():
    """
    Input: I O M K I L O L I K T C J I O P L L P O

    Actual Output:
        OPLLPO
        KILOLIK

    Output:
        ILOLI
        OPLLPO
        KILOLIK
    """
    palindrome_string = raw_input('Enter Palindrome String?\n')
    palindrome_string = "".join(palindrome_string.split())
    length_of_palindrome, palindrome_dict = len(palindrome_string), {}
    reversed_number, length_of_assuming = None, 4
    for j in xrange(4, length_of_palindrome + 1):
        for i in xrange(1, length_of_palindrome + 1):
            string = palindrome_string[i - 1 : j + i]
            if len(string) >= 4:
                value = isPalindrome(string)
                if value:
                    palindrome_dict[string] = string
    return palindrome_dict

def isPalindrome(string):
    """
    Check the string is palindrome or not

    """
    if string == reverse(string):
        return True
    else:
        return False


if __name__ == "__main__":
    palindrome_dict = get_no_of_possible_palindromes()
    for key, palindrome in palindrome_dict.items():
        print palindrome

