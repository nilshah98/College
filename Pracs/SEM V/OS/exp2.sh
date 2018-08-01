#!/bin/bash
lines=$(wc -l < users.txt)
for i in $(seq 1 $lines)
do
	newuser=$(sed "${i}q;d" users.txt)
	sudo useradd $newuser
done 
