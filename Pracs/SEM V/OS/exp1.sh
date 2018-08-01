#!/bin/bash
function simpleops {
	echo enter two numbers
	read a
	read b
	echo addition
	echo $(($a+$b))
	echo subtraction
	echo $((a-b))
	echo multiplication
	echo $(expr "$a" \* "$b")
	echo division
	echo $(($a/$b))
	echo comparison
	echo $(($a>$b))
	echo logical
	echo $((a&b))
}

function factorial {
	echo enter number to find factorial-
	read a
	ans=1
	for x in $(seq 1 $a)
	do
		ans=$(($ans*$x))	
	done
	echo factorial is-
	echo $ans
}

function prime {
	echo enter number check if prime
	read a
	for x in $(seq 2 $a)
	do
		mod=$((a%x))
		if [ $mod == '0' ]
			then
			break
		fi
	done
	if [ $x == $a ]
		then
		echo prime number
	else
		echo not prime
	fi
}
