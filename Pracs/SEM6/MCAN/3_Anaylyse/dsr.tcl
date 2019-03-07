# simple-wireless.tcl
# A simple example for wireless simulation

# ======================================================================
# Define options
# ======================================================================
set val(chan)           Channel/WirelessChannel    ;# channel type
set val(prop)           Propagation/TwoRayGround   ;# radio-propagation model
set val(netif)          Phy/WirelessPhy            ;# network interface type
set val(mac)            Mac/802_11                 ;# MAC type
set val(ifq)            Queue/DropTail/PriQueue    ;# interface queue type
set val(ll)             LL                         ;# link layer type
set val(ant)            Antenna/OmniAntenna        ;# antenna model
set val(ifqlen)         10                         ;# max packet in ifq
set val(nn)             10                          ;# number of mobilenodes
set val(rp)             DSR                       ;# routing protocol
set val(x)		500
set val(y)		500
# ======================================================================
# Main Program
# ======================================================================


#
# Initialize Global Variables
#
set ns_		[new Simulator]
set tracefd     [open simple.tr w]
$ns_ trace-all $tracefd

set namtrace [open simple-wireless.nam w]
$ns_ namtrace-all-wireless $namtrace $val(x) $val(y)

# set up topography object
set topo       [new Topography]

$topo load_flatgrid 500 500

#
# Create God
#
create-god $val(nn)

#
#  Create the specified number of mobilenodes [$val(nn)] and "attach" them
#  to the channel. 
#  Here two nodes are created : node(0) and node(1)

# configure node

        $ns_ node-config -adhocRouting $val(rp) \
			 -llType $val(ll) \
			 -macType $val(mac) \
			 -ifqType $val(ifq) \
			 -ifqLen $val(ifqlen) \
			 -antType $val(ant) \
			 -propType $val(prop) \
			 -phyType $val(netif) \
			 -channelType $val(chan) \
			 -topoInstance $topo \
			 -agentTrace ON \
			 -routerTrace ON \
			 -macTrace OFF \
			 -movementTrace OFF			
			 
	for {set i 0} {$i < $val(nn) } {incr i} {
		set node_($i) [$ns_ node]	
		$node_($i) random-motion 0		;# disable random motion
	}

#
# Provide initial (X,Y, for now Z=0) co-ordinates for mobilenodes
$node_(0)	set X_ 307
$node_(0)	set Y_ 247
$node_(0)	set Z_ 0
$node_(1)	set X_ 129
$node_(1)	set Y_ 389
$node_(1)	set Z_ 0
$node_(2)	set X_ 353
$node_(2)	set Y_ 179
$node_(2)	set Z_ 0
$node_(3)	set X_ 414
$node_(3)	set Y_ 211
$node_(3)	set Z_ 0
$node_(4)	set X_ 116
$node_(4)	set Y_ 46
$node_(4)	set Z_ 0
$node_(5)	set X_ 380
$node_(5)	set Y_ 330
$node_(5)	set Z_ 0
$node_(6)	set X_ 231
$node_(6)	set Y_ 302
$node_(6)	set Z_ 0
$node_(7)	set X_ 415
$node_(7)	set Y_ 25
$node_(7)	set Z_ 0
$node_(8)	set X_ 233
$node_(8)	set Y_ 387
$node_(8)	set Z_ 0
$node_(9)	set X_ 254
$node_(9)	set Y_ 287
$node_(9)	set Z_ 0
# Setup traffic flow between nodes
# TCP connections between node_(0) and node_(1)

set tcp [new Agent/TCP]
$tcp set class_ 2
set sink [new Agent/TCPSink]
$ns_ attach-agent $node_(0) $tcp
$ns_ attach-agent $node_(1) $sink
$ns_ connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns_ at 10.0 "$ftp start" 

set tcp [new Agent/TCP]
$tcp set class_ 2
set sink [new Agent/TCPSink]
$ns_ attach-agent $node_(2) $tcp
$ns_ attach-agent $node_(3) $sink
$ns_ connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns_ at 15.0 "$ftp start" 


set tcp [new Agent/TCP]
$tcp set class_ 2
set sink [new Agent/TCPSink]
$ns_ attach-agent $node_(4) $tcp
$ns_ attach-agent $node_(5) $sink
$ns_ connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns_ at 20.0 "$ftp start" 


set tcp [new Agent/TCP]
$tcp set class_ 2
set sink [new Agent/TCPSink]
$ns_ attach-agent $node_(6) $tcp
$ns_ attach-agent $node_(7) $sink
$ns_ connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns_ at 25.0 "$ftp start" 


set tcp [new Agent/TCP]
$tcp set class_ 2
set sink [new Agent/TCPSink]
$ns_ attach-agent $node_(8) $tcp
$ns_ attach-agent $node_(9) $sink
$ns_ connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns_ at 30.0 "$ftp start" 


#
# Tell nodes when the simulation ends
#
for {set i 0} {$i < $val(nn) } {incr i} {
    $ns_ at 150.0 "$node_($i) reset";
}
$ns_ at 150.0 "stop"
$ns_ at 150.01 "puts \"NS EXITING...\" ; $ns_ halt"
proc stop {} {
    global ns_ tracefd
    $ns_ flush-trace
    close $tracefd
    exec nam simple-wireless.nam & 
}

puts "Starting Simulation..."
$ns_ run

