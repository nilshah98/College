#!/bin/bash

#Setting the initial variables

IFILE="$HOME/Desktop/Shivam/bday.csv"
OFILE="bday_out"$$
MAILID="shivam.pawase@somaiya.edu"

# Retrieving today's date and month

DAT=`date '+%d %b'`
DAY=$(echo $DAT| cut -c 1-2)
MON=`echo $(echo $DAT| cut -c 4-6) | awk '{print toupper($0);}'`

# Reading the bday.csv file and finding the users whose 
# date matches with today and writing to OFILE

while IFS=",-" read name day month year
do
        day=`printf "%02d\n" $day`
        month=`echo $month |  awk '{print toupper($0);}'`
        if [ $day -eq $DAY -a $month = $MON ]
        then
             echo $name
        fi
done < $IFILE > $OFILE

#If OFILE has some data, header is added and the file
#is mailed to the respective users in MAILID.

if [ -f $OFILE -a -s $OFILE ]
then
   sed -i '1i The following users celebrate their birthday:\n' $OFILE
   mailx -s "Birthday on: $DAT" $MAILID  < $OFILE
   \rm $OFILE
   echo "Birthday mail sent"
else
   echo "No birthdays today"
fi

