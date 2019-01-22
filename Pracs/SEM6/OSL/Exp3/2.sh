#!/bin/bash

a=$1
b=$2
c=$3

if [ $a -ge $b ]
then
	if [ $a -ge $c ]
	then
		echo "a is maximum"
	else
		echo "c is maximum"
		echo "b is minimum"
	fi
	if [ $b -ge $c ]
	then 
		echo "c is minimum"
	fi
elif [ $b -ge $c ]
then
	echo "b is maximum"
	if [ $a -ge $c ]
	then
		echo "c is minimum"
	else 
		echo "a is minimum"
	fi
else
	echo "c is maximum"
	echo "a is minimum"
fi
