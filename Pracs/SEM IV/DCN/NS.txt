#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows
$ns color 1 Blue
$ns color 2 Red

#Open the nam trace file
set nf [open out.nam w]
$ns namtrace-all $nf

#Define a 'finish' procedure
proc finish {} {
        global ns nf
        $ns flush-trace
	#Close the trace file
        close $nf
	#Execute nam on the trace file
        exec nam out.nam &
        exit 0
}

#Create four nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

#Create links between the nodes
$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n3 $n2 1Mb 20ms SFQ
$ns duplex-link $n3 $n4 1Mb 10ms DropTail
$ns duplex-link $n3 $n5 1Mb 10ms DropTail

#animation purpose so that we get the accurate design we want
$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n5 orient right-down

#Monitor the queue for the link between node 2 and node 3
$ns duplex-link-op $n2 $n3 queuePos 0.5



#create a TCP agent and attach it to node n0
set tcp1 [new Agent/TCP]
$tcp1 set class_ 1
$ns attach-agent $n0 $tcp1
#create a FTP over TCP and attach it to tcp1
set ftp [new Application/FTP]
$ftp attach-agent $tcp1


#Create a UDP agent and attach it to node n1
set udp1 [new Agent/UDP]
$udp1 set class_ 2  #class_2 is used to attach color 2 to the UDP agent
$ns attach-agent $n1 $udp1

# Create a CBR traffic source and attach it to udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 500
$cbr1 set interval_ 0.005
$cbr1 attach-agent $udp1

#create a SINK agent and attach it to node n4
set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink

#Create a Null agent (a traffic sink) and attach it to node n5
set null0 [new Agent/Null]
$ns attach-agent $n5 $null0

#Connect the traffic sources with the traffic sink  
$ns connect $udp1 $null0
$ns connect $tcp1 $sink 

#Schedule events for the CBR agents
$ns at 0.5 "$ftp start"
$ns at 1.5 "$cbr1 start"
$ns at 4.0 "$cbr1 stop"
$ns at 4.5 "$ftp stop"
#Call the finish procedure after 5 seconds of simulation time
$ns at 5.0 "finish"

#Run the simulation
$ns run
