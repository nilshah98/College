#!/bin/bash

echo "Enter n:"
read n
temp=$n

max=-100
min=1000

while [ $temp -ne 0 ]
do
	echo "Enter number:"
	read num
	if [ $num -gt $max ]
	then
		max=`expr $num`
	fi
	if [ $num -lt $min ]
	then
		min=`expr $num`
	fi
	temp=`expr $temp - 1`
done

echo "Maximum is $max and minimun is $min"
