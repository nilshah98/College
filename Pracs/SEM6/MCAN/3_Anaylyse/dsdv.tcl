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
set val(ifqlen)         50                         ;# max packet in ifq
set val(nn)             50                          ;# number of mobilenodes
set val(rp)             DSDV                       ;# routing protocol
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
$node_(0)	set X_ 215
$node_(0)	set Y_ 366
$node_(0)	set Z_ 0
$ns_ at 95 "$node_(0) setdest 207 407 0"
$node_(1)	set X_ 72
$node_(1)	set Y_ 156
$node_(1)	set Z_ 0
$ns_ at 125 "$node_(1) setdest 412 331 0"
$node_(2)	set X_ 100
$node_(2)	set Y_ 176
$node_(2)	set Z_ 0
$ns_ at 13 "$node_(2) setdest 45 255 0"
$node_(3)	set X_ 3
$node_(3)	set Y_ 245
$node_(3)	set Z_ 0
$ns_ at 63 "$node_(3) setdest 101 244 0"
$node_(4)	set X_ 343
$node_(4)	set Y_ 361
$node_(4)	set Z_ 0
$ns_ at 57 "$node_(4) setdest 20 270 0"
$node_(5)	set X_ 356
$node_(5)	set Y_ 408
$node_(5)	set Z_ 0
$ns_ at 34 "$node_(5) setdest 9 266 0"
$node_(6)	set X_ 284
$node_(6)	set Y_ 267
$node_(6)	set Z_ 0
$ns_ at 87 "$node_(6) setdest 263 121 0"
$node_(7)	set X_ 312
$node_(7)	set Y_ 115
$node_(7)	set Z_ 0
$ns_ at 9 "$node_(7) setdest 166 439 0"
$node_(8)	set X_ 86
$node_(8)	set Y_ 155
$node_(8)	set Z_ 0
$ns_ at 75 "$node_(8) setdest 104 438 0"
$node_(9)	set X_ 233
$node_(9)	set Y_ 82
$node_(9)	set Z_ 0
$ns_ at 110 "$node_(9) setdest 388 409 0"
$node_(10)	set X_ 4
$node_(10)	set Y_ 32
$node_(10)	set Z_ 0
$ns_ at 110 "$node_(10) setdest 240 384 0"
$node_(11)	set X_ 250
$node_(11)	set Y_ 353
$node_(11)	set Z_ 0
$ns_ at 58 "$node_(11) setdest 8 4 0"
$node_(12)	set X_ 35
$node_(12)	set Y_ 432
$node_(12)	set Z_ 0
$ns_ at 39 "$node_(12) setdest 88 257 0"
$node_(13)	set X_ 182
$node_(13)	set Y_ 297
$node_(13)	set Z_ 0
$ns_ at 37 "$node_(13) setdest 46 109 0"
$node_(14)	set X_ 414
$node_(14)	set Y_ 445
$node_(14)	set Z_ 0
$ns_ at 86 "$node_(14) setdest 256 96 0"
$node_(15)	set X_ 330
$node_(15)	set Y_ 71
$node_(15)	set Z_ 0
$ns_ at 55 "$node_(15) setdest 373 291 0"
$node_(16)	set X_ 218
$node_(16)	set Y_ 353
$node_(16)	set Z_ 0
$ns_ at 78 "$node_(16) setdest 439 104 0"
$node_(17)	set X_ 396
$node_(17)	set Y_ 371
$node_(17)	set Z_ 0
$ns_ at 28 "$node_(17) setdest 214 306 0"
$node_(18)	set X_ 102
$node_(18)	set Y_ 426
$node_(18)	set Z_ 0
$ns_ at 118 "$node_(18) setdest 422 415 0"
$node_(19)	set X_ 434
$node_(19)	set Y_ 157
$node_(19)	set Z_ 0
$ns_ at 121 "$node_(19) setdest 394 397 0"
$node_(20)	set X_ 212
$node_(20)	set Y_ 410
$node_(20)	set Z_ 0
$ns_ at 95 "$node_(20) setdest 108 377 0"
$node_(21)	set X_ 294
$node_(21)	set Y_ 271
$node_(21)	set Z_ 0
$ns_ at 110 "$node_(21) setdest 445 368 0"
$node_(22)	set X_ 398
$node_(22)	set Y_ 132
$node_(22)	set Z_ 0
$ns_ at 106 "$node_(22) setdest 65 147 0"
$node_(23)	set X_ 419
$node_(23)	set Y_ 135
$node_(23)	set Z_ 0
$ns_ at 5 "$node_(23) setdest 48 326 0"
$node_(24)	set X_ 269
$node_(24)	set Y_ 391
$node_(24)	set Z_ 0
$ns_ at 104 "$node_(24) setdest 45 20 0"
$node_(25)	set X_ 151
$node_(25)	set Y_ 420
$node_(25)	set Z_ 0
$ns_ at 114 "$node_(25) setdest 353 292 0"
$node_(26)	set X_ 407
$node_(26)	set Y_ 250
$node_(26)	set Z_ 0
$ns_ at 29 "$node_(26) setdest 326 394 0"
$node_(27)	set X_ 441
$node_(27)	set Y_ 277
$node_(27)	set Z_ 0
$ns_ at 37 "$node_(27) setdest 52 446 0"
$node_(28)	set X_ 291
$node_(28)	set Y_ 231
$node_(28)	set Z_ 0
$ns_ at 75 "$node_(28) setdest 303 442 0"
$node_(29)	set X_ 138
$node_(29)	set Y_ 131
$node_(29)	set Z_ 0
$ns_ at 15 "$node_(29) setdest 39 50 0"
$node_(30)	set X_ 384
$node_(30)	set Y_ 414
$node_(30)	set Z_ 0
$ns_ at 61 "$node_(30) setdest 292 217 0"
$node_(31)	set X_ 205
$node_(31)	set Y_ 203
$node_(31)	set Z_ 0
$ns_ at 74 "$node_(31) setdest 366 416 0"
$node_(32)	set X_ 107
$node_(32)	set Y_ 432
$node_(32)	set Z_ 0
$ns_ at 46 "$node_(32) setdest 102 161 0"
$node_(33)	set X_ 265
$node_(33)	set Y_ 418
$node_(33)	set Z_ 0
$ns_ at 63 "$node_(33) setdest 268 219 0"
$node_(34)	set X_ 319
$node_(34)	set Y_ 428
$node_(34)	set Z_ 0
$ns_ at 84 "$node_(34) setdest 298 389 0"
$node_(35)	set X_ 75
$node_(35)	set Y_ 181
$node_(35)	set Z_ 0
$ns_ at 76 "$node_(35) setdest 412 283 0"
$node_(36)	set X_ 422
$node_(36)	set Y_ 13
$node_(36)	set Z_ 0
$ns_ at 26 "$node_(36) setdest 68 137 0"
$node_(37)	set X_ 436
$node_(37)	set Y_ 156
$node_(37)	set Z_ 0
$ns_ at 57 "$node_(37) setdest 156 14 0"
$node_(38)	set X_ 40
$node_(38)	set Y_ 221
$node_(38)	set Z_ 0
$ns_ at 63 "$node_(38) setdest 392 380 0"
$node_(39)	set X_ 31
$node_(39)	set Y_ 31
$node_(39)	set Z_ 0
$ns_ at 75 "$node_(39) setdest 52 422 0"
$node_(40)	set X_ 151
$node_(40)	set Y_ 205
$node_(40)	set Z_ 0
$ns_ at 54 "$node_(40) setdest 217 36 0"
$node_(41)	set X_ 99
$node_(41)	set Y_ 114
$node_(41)	set Z_ 0
$ns_ at 7 "$node_(41) setdest 166 352 0"
$node_(42)	set X_ 168
$node_(42)	set Y_ 198
$node_(42)	set Z_ 0
$ns_ at 22 "$node_(42) setdest 152 286 0"
$node_(43)	set X_ 380
$node_(43)	set Y_ 252
$node_(43)	set Z_ 0
$ns_ at 59 "$node_(43) setdest 210 388 0"
$node_(44)	set X_ 215
$node_(44)	set Y_ 87
$node_(44)	set Z_ 0
$ns_ at 55 "$node_(44) setdest 210 309 0"
$node_(45)	set X_ 246
$node_(45)	set Y_ 228
$node_(45)	set Z_ 0
$ns_ at 107 "$node_(45) setdest 447 289 0"
$node_(46)	set X_ 255
$node_(46)	set Y_ 17
$node_(46)	set Z_ 0
$ns_ at 99 "$node_(46) setdest 341 285 0"
$node_(47)	set X_ 56
$node_(47)	set Y_ 142
$node_(47)	set Z_ 0
$ns_ at 46 "$node_(47) setdest 96 226 0"
$node_(48)	set X_ 191
$node_(48)	set Y_ 392
$node_(48)	set Z_ 0
$ns_ at 16 "$node_(48) setdest 278 386 0"
$node_(49)	set X_ 14
$node_(49)	set Y_ 195
$node_(49)	set Z_ 0
$ns_ at 38 "$node_(49) setdest 328 125 0"
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

