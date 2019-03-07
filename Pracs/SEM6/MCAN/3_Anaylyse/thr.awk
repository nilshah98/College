BEGIN {
	recvdSize = 0
	startTime = 1
	stopTime = 0
	sent=0
	receive=0
}

{
	event = $1
	time = $2
	node_id = $3
	pkt_size = $8
	level = $4

	if (level == "AGT" && event == "s" && $7 == "tcp") {
        sent++	
	if (time < startTime) {
		startTime = time
		}
	}
	
	if (level == "AGT" && event == "r" && $7 == "tcp") {
	    receive++
	if (time > stopTime) {
		stopTime = time
		}
	recvdSize += pkt_size
        }
}
	
END {
printf("sent_packets\t d",sent);	
printf("\nreceived_packets %d",receive);
#printf("\nPDR %.2f%",(receive/sent)*100);		
printf("\nAverage Throughput[kbps] = %.2f\t StartTime=%.2f\t StopTime = %.2f\n", (recvdSize/(stopTime-startTime))*(8/1000),startTime,stopTime);
}
