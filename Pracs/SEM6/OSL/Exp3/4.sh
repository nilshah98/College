#!/bin/bash

curr=$(date +"%H")

if [ $curr -le 12 ]
then
	echo "Good Morning"
elif [ $curr -le 16 ]
then
	echo "Good Afternoon"
elif [ $curr -le 20 ]
then 
	echo "Good Evening"
elif [ $curr -le 23 ]
then
	echo "Good Night"
fi
