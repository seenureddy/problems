#!/bin/bash

show_answer=true
while [ $# -gt 0 ]; do
  	case "$1" in
    	-y)
    	  	show_answer=false
      	;;
  	esac
	shift
done

if $show_answer ; then
	echo "WARNING!! This script REMOVE your galle's database and you LOSE all the data."
	read -p "Are you sure you want to delete all data? (Press Y to continue): " -n 1 -r
	echo    # (optional) move to a new line
	if [[ ! $REPLY =~ ^[Yy]$ ]] ; then
		exit 1
	fi
fi

echo "-> Remove galle DB"
dropdb galledb
echo "-> Create galle DB"
createdb galledb

echo "-> Load migrations"
python manage.py migrate

echo "-> Load collectstatic"
python manage.py collectstatic --no-input

echo "-> Check testing"
python manage.py test
