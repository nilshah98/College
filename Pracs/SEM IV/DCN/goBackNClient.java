import java.io.*;
import java.net.*;
import java.util.*;

public class goBackNClient {
public static void main(String[] args) {
int currWindow = 0;
int currFrame = 0;
int totFrame = 10;
int totWindow = 1;

Random r = new Random();
int messageLost = r.nextInt(10);

while(currWindow<totWindow){
    try{
        Socket s=new Socket();
        s.connect(new InetSocketAddress("localhost", 6666));
        // Creating input and output streams
        DataOutputStream dout=new DataOutputStream(s.getOutputStream());
        DataInputStream dis=new DataInputStream(s.getInputStream());
        // Sending message and recieveing ACK
        System.out.println("Current window: "+currWindow);
        
        currFrame = 0;
        while(currFrame<totFrame){
            Thread.sleep(100);
            dout.writeUTF(String.valueOf(currFrame));
            System.out.println("Sent frame: "+currFrame);
            dout.flush();
            currFrame++;
        }
		Boolean flag = true;
        currFrame = 0;
        Vector<Integer> framesLost = new Vector<Integer>();
        while(currFrame<totFrame){
            Thread.sleep(500);
            String str=(String)dis.readUTF();
            if(Integer.valueOf(str)<0){
		Thread.sleep(1000);
                framesLost.add(Integer.valueOf(currFrame));
				System.out.println("Frame recvd out of order");
				flag = false;
            }else if(flag){System.out.println("ACK:"+str);}
            currFrame++;
        }
        // System.out.println(framesLost.size());
        if(framesLost.size()>0){
            if(framesLost.lastElement()==9){
                // Then qualifies for retransmission
                currFrame=framesLost.firstElement();
                // Retransmission
                System.out.println("Retransmiting, since ack not recvd");
                System.out.println("Current window: "+currWindow);

                while(currFrame<10){
                    Thread.sleep(100);
                    dout.writeUTF(String.valueOf(currFrame));
                    System.out.println("ReSent frame: "+currFrame);
                    dout.flush();
                    currFrame++;        
                }

                currFrame=framesLost.firstElement();
                // Recieve Ack
                while(currFrame<10){
                    Thread.sleep(500);
                    String str=(String)dis.readUTF();
                    System.out.println("ACK:"+str);
                    currFrame++;                
                }
            }
        }

        dout.close();
        dis.close();
        s.close();

    }catch(Exception e){
        System.out.println("Connection timed out, no ack recvd.");
    }

    currWindow++;
    }
}
}
