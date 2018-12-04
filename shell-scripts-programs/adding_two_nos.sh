# /bin/bash

# Script to sum of two nos

if [ $# -ne 2 ]
then
    echo "Usage - $0   x    y"
    echo "        Where x and y are two nos for which I will print sum"
    exit 1
fi
    echo "Sum of $1 and $2 is `expr $1 + $2`\n"
