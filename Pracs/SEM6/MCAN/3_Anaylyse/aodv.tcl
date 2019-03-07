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
set val(ifqlen)         20                         ;# max packet in ifq
set val(nn)             20                          ;# number of mobilenodes
set val(rp)             AODV                       ;# routing protocol
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
$node_(0)	set X_ 353
$node_(0)	set Y_ 307
$node_(0)	set Z_ 0
$ns_ at 45 "$node_(0) setdest 309 258 0"
$node_(1)	set X_ 273
$node_(1)	set Y_ 248
$node_(1)	set Z_ 0
$ns_ at 39 "$node_(1) setdest 137 437 0"
$node_(2)	set X_ 417
$node_(2)	set Y_ 151
$node_(2)	set Z_ 0
$ns_ at 12 "$node_(2) setdest 177 211 0"
$node_(3)	set X_ 95
$node_(3)	set Y_ 28
$node_(3)	set Z_ 0
$ns_ at 104 "$node_(3) setdest 188 93 0"
$node_(4)	set X_ 379
$node_(4)	set Y_ 58
$node_(4)	set Z_ 0
$ns_ at 24 "$node_(4) setdest 100 122 0"
$node_(5)	set X_ 221
$node_(5)	set Y_ 360
$node_(5)	set Z_ 0
$ns_ at 33 "$node_(5) setdest 128 449 0"
$node_(6)	set X_ 275
$node_(6)	set Y_ 423
$node_(6)	set Z_ 0
$ns_ at 96 "$node_(6) setdest 439 402 0"
$node_(7)	set X_ 237
$node_(7)	set Y_ 436
$node_(7)	set Z_ 0
$ns_ at 107 "$node_(7) setdest 308 421 0"
$node_(8)	set X_ 1
$node_(8)	set Y_ 294
$node_(8)	set Z_ 0
$ns_ at 100 "$node_(8) setdest 348 110 0"
$node_(9)	set X_ 449
$node_(9)	set Y_ 237
$node_(9)	set Z_ 0
$ns_ at 57 "$node_(9) setdest 412 307 0"
$node_(10)	set X_ 63
$node_(10)	set Y_ 262
$node_(10)	set Z_ 0
$ns_ at 42 "$node_(10) setdest 307 210 0"
$node_(11)	set X_ 441
$node_(11)	set Y_ 373
$node_(11)	set Z_ 0
$ns_ at 7 "$node_(11) setdest 446 24 0"
$node_(12)	set X_ 107
$node_(12)	set Y_ 186
$node_(12)	set Z_ 0
$ns_ at 121 "$node_(12) setdest 360 28 0"
$node_(13)	set X_ 402
$node_(13)	set Y_ 263
$node_(13)	set Z_ 0
$ns_ at 90 "$node_(13) setdest 189 16 0"
$node_(14)	set X_ 58
$node_(14)	set Y_ 223
$node_(14)	set Z_ 0
$ns_ at 110 "$node_(14) setdest 397 77 0"
$node_(15)	set X_ 54
$node_(15)	set Y_ 234
$node_(15)	set Z_ 0
$ns_ at 28 "$node_(15) setdest 325 314 0"
$node_(16)	set X_ 365
$node_(16)	set Y_ 329
$node_(16)	set Z_ 0
$ns_ at 45 "$node_(16) setdest 320 351 0"
$node_(17)	set X_ 243
$node_(17)	set Y_ 154
$node_(17)	set Z_ 0
$ns_ at 76 "$node_(17) setdest 284 357 0"
$node_(18)	set X_ 39
$node_(18)	set Y_ 388
$node_(18)	set Z_ 0
$ns_ at 115 "$node_(18) setdest 65 255 0"
$node_(19)	set X_ 93
$node_(19)	set Y_ 261
$node_(19)	set Z_ 0
$ns_ at 62 "$node_(19) setdest 88 40 0"
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

