#!/bin/bash

echo "Enter a:"
read a
echo "Enter b:"
read b

if [ $a -gt $b ]
then
	echo "a is maximum and b is minimum"
elif [ $b -gt $a ]
then
	echo "a is minimum and b is maximum"
else
	echo "Both are equal"
fi
