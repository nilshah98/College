import java.io.*;
import java.net.*;
import java.util.*;

public class MyClient {
public static void main(String[] args) {
int i = 0;
Random rand = new Random();
int messageLost = rand.nextInt(10);
while(i<10){
	try{
	Socket s=new Socket();
	s.connect(new InetSocketAddress("localhost", 6666), 3000);
	// Creating input and output streams
	DataOutputStream dout=new DataOutputStream(s.getOutputStream());
	DataInputStream dis=new DataInputStream(s.getInputStream());
	// Sending message and recieveing ACK



	if(i!=messageLost){
	    dout.writeUTF(String.valueOf(i));
	    dout.flush();
	    Thread.sleep(500);
	    String str=(String)dis.readUTF();
	    System.out.println("ACK:"+str);
	    i++;
	}
	else{
		// System.out.println("xxxxxx");
		messageLost=100;
		Thread.sleep(3100);
	}


	dout.close();
	dis.close();
	s.close();

	}catch(Exception e){
		System.out.println("Connection timed out, no ack recvd.");
	}
	}
}
}
