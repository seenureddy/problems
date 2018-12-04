# /bin/bash

set -e

echo 'PATH ..........'

HOME_ROOT=$(pwd)
echo $HOME_ROOT

echo 'End of the path pick .........'

echo 'Local variables'

HELLO=Hello

function hello {
    local HELLO=world
    echo $HELLO
}

echo $HELLO
hello
echo $HELLO

echo 'END OF LOCAL VARIABLES.......'

echo 'Conditionals .............'

if [ "foo" == "foo" ]; then

    echo expression is evaluated to true

else

   echo expression is evaluated to false
fi


echo Conditionals with variables

t1="foo"
t2="bar"

if [ '$t1' == '$t2' ]; then

    echo expression is evaluated to true

else

    echo expression is evaluated to false

fi

echo loops for, while and until

echo start for loop

for i in $(ls); do
    echo item: $i
done

echo C-like for loop

for i in `seq 1 10`;

do 
    echo $i
done

echo end of C-like for


echo While loop

COUNTER=0

while [ $COUNTER -lt 10 ]; do

    echo The counter is $COUNTER

    let COUNTER=COUNTER+1
done

echo end of while loop


echo Until loop

COUNTER=20

until [ $COUNTER -lt 10 ]; do
    
    echo The COUNTER is $COUNTER

    let COUNTER-=1

done

echo end of until loop    
 
