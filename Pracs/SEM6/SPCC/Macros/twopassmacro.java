import java.util.*;
import java.io.*;
import java.lang.*;

class Pair {
    String param="",mname="";
    public Pair(String param,String mname) {
        this.param=param;
        this.mname=mname;
    }
}
class twopassmacro {
    static HashMap<String,Integer> mnt=new HashMap();
    static HashMap<Integer,String> mdt = new HashMap();
    static HashMap<String,Pair> ala= new HashMap();
    static HashMap<String,String> ald= new HashMap();
    static ArrayList<String> pass2out=new ArrayList();
    static File file = null;
    static String s="";
    static String[] lines = new String[200];
    static String[] tokens = new String[50];
    static int l=0;
    static int mntc=0,mdtc=0;
    //static int ind=1;
	public static void main(String args[]) {
        //file = new File("inputmacro.txt");
        BufferedWriter bw = null;
        FileWriter fw = null;

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("inputmacro.txt")));
            while((s=br.readLine())!=null) {
                if(!s.trim().isEmpty()) {
                    lines[l]=s;
                    l++;
                }
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("OUTPUT OF PASS1\n");
        pass1();
        System.out.println("\nOUTPUT OF PASS2\n");
        pass2();
	}

    public static void pass1() {
        int lt = 0;
        int c=0;
        String str="";
        while(lt<l) {
            c=read(lines[lt]);

            if(tokens[0].equals("MACRO")) {
                //System.out.println("1: "+lt);
                int ind=1;
                lt++;
                str=lines[lt];
                c=read(lines[lt]);
                int fl=1;
                String name="";
                int keyw=0;
                while(!tokens[0].equals("MEND")) {
                    /*for(int i=0;i<c;i++)
                        System.out.print(tokens[i]+" ");
                    System.out.println();*/
                    String content=lines[lt];
                    String params[] = new String[10];

                    int i=0;
                    if(c==3) 
                        i=1;
                    //Insert into mnt
                    params=tokens[i+1].split(",");
                    if(fl==1) {
                        //System.out.println(tokens[i]+" "+(lt+1));
                        name=tokens[i];
                        mnt.put(tokens[i],(lt+1));
                        //Put parameters in ala and ald
                        constructala(params,name);

                        //Check for keyword args
                        if(tokens[i+1].contains("="))
                            keyw=1;
                    }

                    if(fl==0 && keyw!=1) 
                        content=reconstructmdt(name,content);

                    fl=0;
                    mdt.put(lt,content);
                    
                    //End 
                    lt++;
                    c=read(lines[lt]);
                }
                if(tokens[0].equals("MEND")) {
                    mdt.put(lt,lines[lt]);
                    lt++;
                }
            }
            else {
                //System.out.println("2: "+lt);
                lt++;
                continue;
            }
        }


        //Pass 1 output
        pass1op();
        
    }

    public static void pass2() {
        int lt=0;
        String pass2op="";
        int c=0;
        String prev="";
        while(lt<l) {
            c=read(lines[lt]);
            int i=0;
            if(c==3)
                i=1;
            if(mnt.containsKey(tokens[i]) && !prev.equals("MACRO")) {
                //System.out.println("h"+" "+tokens[i]+" "+lt);
                mdtc=mnt.get(tokens[i]);
                //mdtc++;
                int ind=1;

                //Reconstruct ald
                String[] params=tokens[i+1].split(",");
                if(tokens[i+1].contains("=")) {
                    for(String s10:params) {
                        String kv[]=s10.split("=");
                        ald.put(("&"+kv[0]),kv[1]);
                    }
                }
                else {
                    for(String s7:params) {
                        ald.put("#"+ind,s7);
                        ind++;
                    }
                }

                //Expand macro
                String mdl=mdt.get(mdtc);
                while(!mdl.contains("MEND")) {
                    c=read(mdt.get(mdtc));
                    i=0;
                    if(c==3)
                        i=1;

                    for(String s9:ald.keySet()) {
                        if(mdl.contains(s9))
                            mdl=mdl.replaceAll(s9,ald.get(s9));
                    }
                    pass2out.add(mdl);

                    mdtc++;
                    mdl=mdt.get(mdtc);
                }

                lt++;
            }
            else {
                pass2out.add(lines[lt]);
                lt++;
            }
            prev=tokens[0];
        }

        /*for(String s8:ald.keySet()) 
            System.out.println(s8+" "+ald.get(s8));*/

        pass2op();
    }


    public static String reconstructmdt(String name,String content) {
        String val=content;
        if(!val.contains(name)) {
            for(String s5:ala.keySet()) {
                if(val.contains(s5) && ala.get(s5).mname.equals(name)) {
                    val=val.replaceAll(s5,ala.get(s5).param);
                }
            }
        }
        return val;
    }

    public static void constructala(String[] params,String name) {
        //mnt.put(name,index);
        int ind=1;
        for(String s2:params) {
            if(s2.contains("=")) {
                //Keyword parameters
                String valeq[] = s2.split("=");
                if(valeq.length>1) {
                    ala.put(valeq[0],new Pair(valeq[1],name));
                    ald.put(valeq[0],valeq[1]);
                }
                else {
                    ala.put(valeq[0],new Pair("null",name));
                    ald.put(valeq[0],"null");
                }
            }
            else {
                //Positional parameters
                ala.put(s2,new Pair(("#"+ind),name));
                ald.put("#"+ind,s2);
                ind++;
            }
        }
    }

    public static int read(String str) {
        //String str = lines[lt];
        int c=0;
        if(str!=null) {
            StringTokenizer st = new StringTokenizer(str," ",false); 
            while(st.hasMoreTokens()) {
                String temp = st.nextToken();
                if(temp!=null) {
                    tokens[c]=temp;
                    c++;
                }
            }
        }
        return c;
    }

    public static void pass2op() {
        for(String str1:pass2out) {
            if(str1!=null) 
                System.out.println(str1);
        }
    }

    public static void pass1op() {
        System.out.println("** Input Code **");
        for(String s1:lines) {
            if(s1!=null)
                System.out.println(s1);
        }

        System.out.println("\n** MNT **");
        System.out.println("Macro Name.\tLine No.");
        for(String str1:mnt.keySet())
            System.out.println(str1+"\t\t"+mnt.get(str1));

        System.out.println("\n** MDT **");
        System.out.println("Line No.\tStatement");
        for(Integer in:mdt.keySet())
            System.out.println((in+1)+"\t"+mdt.get(in));
        System.out.println();

    }
}