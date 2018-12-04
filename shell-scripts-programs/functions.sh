#! /bin/bash

set -e

echo fucntion

function quit {
    echo exit command is calling
    exit
}


function hello {
    echo Hello!
}

hello
#quit
echo foo end \n

echo Function with parameters

function quit {

   exit
}

function hello {

    echo $1
}

hello h
hello 2
quit 
echo foo \n
