# /bin/bash/

# printing the numbers 5 4 3 2 1 using while loop

i=5
while test $i != 0
do
	echo "$i
"
	i=`expr $i - 1`
done