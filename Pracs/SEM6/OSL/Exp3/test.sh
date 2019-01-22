DAT=`date '+%d %b'`
DAY=$(echo $DAT| cut -c 1-2)
echo $DAY
MON=`echo $(echo $DAT| cut -c 4-6) | awk '{print toupper($0);}'`
echo $MON
