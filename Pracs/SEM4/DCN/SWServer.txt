import java.io.*;
import java.net.*;
import java.util.*;

public class server {
public static void main(String[] args){
int i=0;
while(i<10){
try{
ServerSocket ss=new ServerSocket(6666);
// Thread.sleep(300);
ss.setSoTimeout(3000);

Socket s=ss.accept();//establishes connection

// Create input and output streams.
DataInputStream dis=new DataInputStream(s.getInputStream());
DataOutputStream dout=new DataOutputStream(s.getOutputStream());
// Recevieving message and sending ACK


String str=(String)dis.readUTF();
if(Integer.valueOf(str)==i){
    System.out.println("packet recvd: "+str);
    dout.writeUTF(String.valueOf(i+1));
    dout.flush();
    i++;	
}


dout.close();
dis.close();
ss.close();

}catch(Exception e){
	System.out.println("Connection timed out, no packets recvd.");
}
}
}
}
