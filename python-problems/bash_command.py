#!/usr/bin/python
"""

RedHat Coding question
The following bash pipeline determines the frequency with which different words occur in a
given input.  It outputs the most frequent words, along with their frequencies.
    tr -s ' ' '\n' | sort | uniq -c | sort -n | tail
An example invocation is as follows (of course, on your computer the exact results may vary):
$ cat /usr/share/doc/coreutils-common/README | tr -s ' ' '\n' | sort | uniq -c | sort -n | tail
15 is
18 as
23 that
Implement an equivalent in Python.  You should use only the python standard library, and you must not
use the exec library.  For a varied set of potential inputs, the output should be as close as
reasonable to that of the bash pipeline.

"""

import sys, os
import operator


def implement_bash_command(file_name):
    
    try:
        with open(_arg, 'r') as _file:
            d = dict()
            for line_data in _file.readlines():
                # Loop through each line of the file
                for line_data_list in line_data.splitlines():
                    for line in line_data_list.split(" "):
                        # Remove the leading spaces and newline character
                        line = line.rstrip()
                
                        # Convert the characters in line to 
                        # lowercase to avoid case mismatch
                        lines = line.lower()

                        # Split the line into words
                        words = line.split("\n")

                        # Iterate over each word in line
                        for word in words:
                            # Check if the word is already in dictionary
                            if word == '':
                                continue
                            word_lower = word
                            if word_lower in d:
                                # Increment count of word by 1
                                d[word_lower] = d[word_lower] + 1
                            else:
                                # Add the word to dictionary with count 1
                                d[word_lower] = 1
            
            # Print the contents of dictionary
            for key, _ in sorted(d.items(), key=operator.itemgetter(1), reverse=True)[:10]:
                if d[key] > 1:
                    print(" "*3 + str(d[key]), key)
                
    except IOError as _err:
        sys.stderr.write(os.path.basename(sys.argv[0]) + ": " + _arg + ": " + _err.strerror + "\n")

if __name__ == "__main__":
    for _arg in sys.argv[1:]:
       implement_bash_command(_arg)
