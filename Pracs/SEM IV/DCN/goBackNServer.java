import java.io.*;
import java.net.*;
import java.util.*;

public class goBackNServer {
public static void main(String[] args){
int currWindow = 0;
int currFrame = 0;
int totFrame = 10;
int totWindow = 1;

Random r = new Random();
int ackLost = r.nextInt(10);

while(currWindow<totWindow){
try{
// taking input for 1 window
	ServerSocket ss=new ServerSocket(6666);

	Socket s=ss.accept();//establishes connection

	// Create input and output streams.
	DataInputStream dis=new DataInputStream(s.getInputStream());
	DataOutputStream dout=new DataOutputStream(s.getOutputStream());
	// Recevieving message and sending ACK
	currFrame = 0;

	System.out.println("Current window: "+currWindow);

	while(currFrame<totFrame){
		
		String str=(String)dis.readUTF();
		currFrame++;
	}
	// sending acknowledgement here:	
	currFrame = 0;
	while(currFrame<totFrame){
		Thread.sleep(100);
	    if(currFrame!=ackLost && currFrame!=9){
			dout.writeUTF(String.valueOf(currFrame+1));
			Thread.sleep(500);
			System.out.println("packet recvd: "+currFrame);
			Thread.sleep(100);
	    	System.out.println("Sent ACK: " + currFrame);
	    }
	    else{
		System.out.println("packet recvd: "+currFrame);
		System.out.println("Sent ACK: " + currFrame);
	    dout.writeUTF(String.valueOf(-1));
	    }
	    dout.flush();
	    currFrame++;		
	}

	Vector<Integer> framesLost = new Vector<Integer>();
	framesLost.add(ackLost);
	framesLost.add(9);

    if(framesLost.size()>0){
        if(framesLost.lastElement()==9){
            // Then qualifies for retransmission
            currFrame=framesLost.firstElement();
            // Retransmission
            System.out.println("Recving again");
            System.out.println("Current window: "+currWindow);

            while(currFrame<10){
                Thread.sleep(100);
                String str=(String)dis.readUTF();
                System.out.println("Recvd frame: "+str);
                dout.flush();
                currFrame++;        
            }

            currFrame=framesLost.firstElement();
            // Recieve Ack
            while(currFrame<10){
			Thread.sleep(500);
			System.out.println("packet recvd: "+currFrame);
			Thread.sleep(100);
	    	System.out.println("Sent ACK: " + currFrame);
                currFrame++;                
            }
        }
    }

	dout.close();
	dis.close();
	ss.close();	


}catch(Exception e){
	System.out.println("Connection timed out, no packets recvd.");
}
	currWindow++;
}
}
}
