const readline = require('readline');

rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var arrivalTime;
var burstTime;
var timeSlice;
var processNum;

rl.question('Enter space separated arrival time for jobs ', (answer) => {
	arrivalTime = answer;
	burst();
});

burst = function(){
rl.question('Enter space separated burst time for jobs ', (answer) => {
	burstTime = answer;
	time();
})};

time = function(){
rl.question('Enter time slice for jobs ', (answer) => {
	timeSlice = answer;
	processx();
	rl.close();
})};

processx = function(){
arrivalTime = arrivalTime.split(" ").map(x => parseInt(x));
arrivalC = arrivalTime.slice();
arrivalTime = arrivalTime.map((x,i) => [x,i+1]);

burstTime = burstTime.split(" ").map(x => parseInt(x));
burstC = burstTime.slice();

timeSlice = parseInt(timeSlice);
queue = [];
var totalProcess = burstTime.length;

var ready = [0];
var currTime = 0;
var index;

while( burstTime.reduce((a,b) => a+b,0) > 0 ){
	index = ready[0];
	for(var i = 0; i < Math.min(timeSlice, burstTime[index]); i++){
		queue.push(index+1);
		currTime += 1;

		for(var j=0; j < totalProcess; j++){
			if(ready.indexOf(j) == -1 && currTime >= arrivalTime[j][0] && burstTime[index] > 0){
				ready.push(j);
			}
		}
	}
	var ret;
	ret = ready.splice(0,1)[0];
	burstTime[ret] -= Math.min(burstTime[ret],timeSlice);
	if(burstTime[ret] > 0){
		ready.push(ret);
	}
}
console.log(queue);
finalCalc(queue,arrivalC,burstC,totalProcess);
}


finalCalc = function(queue,arrival,burst,total){
var end = []
for(var i = 1; i<total+1; i++){
	end.push(queue.length - queue.reverse().indexOf(i));
	queue.reverse();
	}
var wait = [];
var turn = [];
var nTurn = [];

for(var i = 0; i<end.length; i++){
	turn.push(end[i] - arrival[i]);
	wait.push(turn[i] - burst[i]);
	nTurn.push(turn[i]/burst[i]);
}
console.log("Waiting Time");
console.log(wait);
console.log("Turnaround Time");
console.log(turn);
console.log("Normalised Turnaround Time");
console.log(nTurn);
console.log("Average Wait-");
console.log(wait.reduce((a,b)=> a+b,0)/total)
console.log("Average Turn-");
console.log(turn.reduce((a,b)=> a+b,0)/total)
console.log("Average nTurn-");
console.log(nTurn.reduce((a,b)=> a+b,0)/total)
}
