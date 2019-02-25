import java.util.*;
import java.io.*;
import java.lang.*;

class Pair {

    String s1,s2;

    public Pair(String s1,String s2) {
        this.s1=s1;
        this.s2=s2;
    }
}

class tblelmnt {
    String symb;
    int val,len;
    char rel;

    public tblelmnt(String s1,int v,int l,char ch) {
        this.symb=s1;
        this.val=v;
        this.len=l;
        this.rel=ch;
    }
}


class twopass {

    static ArrayList<tblelmnt> symbtable= new ArrayList();
    static ArrayList<tblelmnt> litable= new ArrayList();
    static ArrayList<String> pot = new ArrayList();
    static ArrayList<String> pass2out = new ArrayList();
    static HashMap<String,Integer> mot = new HashMap();
    static String[] lines = new String[400];
    static String[] tokens = new String [10];
    static int l=0,vl=0,lc=0;
    static String s="";
    static File file=null;
    public static void main(String args[]) {
		file = new File("PASS1INSTR.txt");
      	library();
        System.out.println("Pass 1 Output\n");
        pass1();
        System.out.println("\n\nPass 2 Output");
//        pass2();
    }

    public static void pass1() {

		BufferedWriter bw = null;
		BufferedWriter bw1 = null;
		FileWriter fw = null;
		FileWriter fw1 = null;


		try {
            BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("PASS1INSTR.txt")));
            while((s=br.readLine())!=null) {
                if(!s.trim().isEmpty()) {
                    lines[l]=s;
                    l++;
                }
            }
        }
        catch(IOException e) { 
            e.printStackTrace();
        }

		for(String str:lines) {
            if(str!=null) {
                StringTokenizer st = new StringTokenizer(str," ",false);
                int c=0;
                while(st.hasMoreTokens()) {
                    tokens[c]=st.nextToken();
                    c++;
                }

                int i=0;
                if(c==3) {
                    i=1;
                }
                char rc;
                if(tokens[i].equals("EQU")) {
                    l=1;
                    rc='A';
                }
                else {
                    l=4;
                    rc='R';
                }
                if(pot.contains(tokens[i])) {
                    switch(tokens[i]) {
                        case "EQU":
                            if(tokens[i+1].equals("*")) 
                                vl=lc;
                            else 
                                vl=Integer.parseInt(tokens[i+1]);
                            break;
                         case "LTORG":
                            while(lc%8!=0)
                                lc++;
                            for(int in=0;in<litable.size();in++) {
                                tblelmnt tb = litable.get(in);
                                litable.set(in,(new tblelmnt(tb.symb,lc,tb.len,'R')));
                                lc+=4;
                            }
                            vl=lc;
                            break;
                         case "DS":
                            int index=tokens[i+1].indexOf("F");
                            int x=0;
                            if(index>0) {
                                x = Integer.parseInt(tokens[i+1].substring(0,tokens[i+1].length()-1));
                                x*=4;
                            }
                            else {
                                String temp=tokens[i+1].substring(0,2);
                                temp=temp.substring(temp.length()-1,temp.length());
                                System.out.println(temp);
                            }
                            lc+=x;
                            break;
                         case "DC":
                            index=tokens[i+1].indexOf("F");
                            x=0;
                            if(index>0) {
                                x = Integer.parseInt(tokens[i+1].substring(0,tokens[i+1].length()-1));
                                x*=4;
                            }
                            else {
                                String temp=tokens[i+1].substring(2,tokens[i+1].length()-2);
                                String[] slist = temp.split(",");
                                for(String si:slist) 
                                    x+=(Integer.parseInt(si));
                            }
                            lc+=x;
                            break;
                    }
                    //symbtable.add(new tblelmnt(tokens[0],vl,l,rc));
                }
                else if(!tokens[i].equals("USING")) {
                    vl=lc;
                    lc+=mot.get(tokens[i]);
                }

                if(i==1)
                    symbtable.add(new tblelmnt(tokens[0],vl,l,rc));

                String[] data = tokens[i+1].split(",");
                if(data.length>1) {
                    if(data[1].charAt(0)=='=')
                        litable.add(new tblelmnt((data[1].substring(1,data[1].length())),0,4,'R'));
                }
            }
        }

		System.out.println("Symbol Table");
        System.out.println("Symbol      Value       Length      R/A");
		String content1 = "";
		String content2 = "";
		
        for(tblelmnt t:symbtable) { 
            if(t.symb.length()<8) {
				content1 += t.symb+" "+t.val+" "+t.len+" "+t.rel+"\n";
            	System.out.println(t.symb+"\t\t"+t.val+"\t"+t.len+"\t\t"+t.rel);
			}
            else {
				content1 += t.symb+" "+t.val+" "+t.len+" "+t.rel+"\n";
                System.out.println(t.symb+"\t"+t.val+"\t"+t.len+"\t\t"+t.rel);
			}
        }
        System.out.println("\n\nLiteral Table");
        System.out.println("Symbol      Value       Length      R/A");
        for(tblelmnt t:litable) { 
            if(t.symb.length()<8) {
				content2 += t.symb+" "+t.val+" "+t.len+" "+t.rel+"\n";	
                System.out.println(t.symb+"\t\t"+t.val+"\t"+t.len+"\t\t"+t.rel);
			}
            else {
				content2 += t.symb+" "+t.val+" "+t.len+" "+t.rel+"\n";
                System.out.println(t.symb+"\t"+t.val+"\t"+t.len+"\t\t"+t.rel);
			}
        }

		try {
			fw = new FileWriter("symb.txt");
			fw1 = new FileWriter("lit.txt");
			bw = new BufferedWriter(fw);
			bw1 = new BufferedWriter(fw1);
			bw.write(content1);
			bw1.write(content2);
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		finally {
			try {
				if(bw!=null) 
					bw.close();
				if(bw1!=null)
					bw1.close();
				if(fw1!=null)
					fw1.close();					
				if(fw!=null)
					fw.close();
			}
			catch(IOException e) { e.printStackTrace(); }
		}

    }

    public static void pass2() {
        BufferedWriter bw = null;
		BufferedWriter bw1 = null;
		FileWriter fw = null;
		FileWriter fw1 = null;
        HashMap<Integer,Integer> bt = new HashMap();
        HashMap<String,String> hp1 = new HashMap();
        //HashMap<String,String> hp2 = new HashMap();
        LinkedHashMap<String,String> hp2=new LinkedHashMap<String,String>();  
        int stn=1;

        try {

            BufferedReader br = new BufferedReader(new FileReader("symb.txt"));
            String in="";
            while((in=br.readLine())!=null) {
                StringTokenizer st1 = new StringTokenizer(in," ",false);
                int cl=0;
                String s1="",s2="";
                while(st1.hasMoreTokens() && cl<2) {
                    if(cl==0)
                        s1=st1.nextToken();
                    else
                        s2=st1.nextToken();
                    cl++;
                }
                if(!s1.equals("") && !s2.equals(""))
                    hp1.put(s1,s2);
            }

            br = new BufferedReader(new FileReader("lit.txt"));
            in="";

            while((in=br.readLine())!=null) {
                StringTokenizer st1 = new StringTokenizer(in," ",false);
                int cl=0;
                String s1="",s2="";
                while(st1.hasMoreTokens() && cl<2) {
                    if(cl==0)
                        s1=st1.nextToken();
                    else
                        s2=st1.nextToken();
                    cl++;
                }
                //System.out.println(s1+" "+s2);
                if(!s1.equals("") && !s2.equals("")) {
                    hp1.put(s1,s2);
                    hp2.put(s1,s2);
                }
            }
        }
        catch(IOException e) {
            e.printStackTrace();
        }

        lc=0;

        System.out.println("\nState no.\tLocation\tInstruction");

        for(String str:lines) {
            if(str!=null) {
                StringTokenizer st = new StringTokenizer(str," ",false);
                int c=0;
                while(st.hasMoreTokens()) {
                    tokens[c]=st.nextToken();
                    c++;
                }

                int lk=0;

                if(c==3)
                    lk=1;

                if(!pot.contains(tokens[lk])) {
                    if(tokens[lk].equals("USING")) {

                        String data[] = tokens[1].split(",");
                        if(data[0].equals("*")) 
                            bt.put(Integer.parseInt(data[1]),0);
                        else {
                            int inv=-1;
                            String val="";
                            if(hp1.containsKey(data[0]))
                                val = hp1.get(data[0]);
                            //System.out.print("h: "+val+" "+data[1]);

                            if(!val.equals("")) {
                                String s1="";
                                if(isInteger(data[1]))
                                    s1=data[1];
                                else if(hp1.containsKey(data[1]))
                                    s1 = hp1.get(data[1]);
                                //System.out.println(s1);
                                if(!s1.equals(""))
                                    bt.put(Integer.parseInt(s1),Integer.parseInt(val));
                            }
                        }
                    }
                    else if(!tokens[lk].equals("END")) {
                        //lc+=mot.get(tokens[0]);
                        String val="";
                        String data[] = tokens[lk+1].split(",");

                        int i=0,inv=-1;

                        if(isInteger(data[0]) && data.length>1)
                            i=1;


                        boolean j=false;
 
                        String cval=data[0];


                        if(data.length>1 && !data[1].equals("")) 
                            j = data[1].contains("INDEX");

                        if(j) {
                            int jin = data[1].indexOf("INDEX");
                            if(jin>2)
                                cval=data[1].substring(0,jin-1);
                        }
                         

                        if(i==0 && data.length>1 && data[1].charAt(0)=='=')  {
                            cval=data[1].substring(1,data[1].length());
                        }
                        else if(i==1)
                            cval=data[1];


                        if(!cval.equals("") && hp1.containsKey(cval))
                            val=hp1.get(cval);
                        int off=-1;
                        int min=2147483647;
                        int mi=-1;

                        boolean flag=true;
                        if(val==null || val.equals("")) 
                            flag=false;

                        //System.out.println(tokens[0]+" "+flag+" "+cval);

                        if(flag) {
                            String op = tokens[0];
                            if(op.charAt(op.length()-1)=='R') {
                                String content="";
                                if(isInteger(data[0]))
                                    content+=data[0];
                                else
                                    content+=hp1.get(data[0]);
                                content+=",";
                                if(isInteger(data[1]))
                                    content+=data[1];
                                else
                                    content+=hp1.get(data[1]);
                                content+="\n";
                                pass2out.add(stn+"\t\t"+lc+"\t\t"+tokens[lk]+"\t"+content);
                            }
                            else {
                                inv=Integer.parseInt(val);

                                int lin = hasLiterals(data);


                                if(lin!=-1) {
                                    String lite = data[lin];
                                    lite=lite.substring(1,lite.length());
                                    inv = Integer.parseInt(hp1.get(lite));
                                }


                                for(int it:bt.keySet()) {
                                    int temp = bt.get(it);
                                    if(Math.abs(inv-temp)<min) {
                                        min=Math.abs(inv-temp);
                                        mi=it;
                                    }
                                }

                                //System.out.println(lin+" "+inv+" "+mi+" "+min);


                                if(mi!=-1) {
                                    String content = "";

                                    if(tokens[lk].equals("BNE"))
                                        content+="7";

                                    else if(isInteger(data[0]))
                                        content+=data[0];
                                    else
                                        content+=hp1.get(data[0]);

                                    //content+=hp1.get(data[i]);

                                    content+=","+min+"(";

                                    if(j==false) {
                                        content+="0,";
                                    }
                                    else
                                        content+=hp1.get("INDEX")+",";
                                    content+=mi+")\n";
                                    if(tokens[lk].equals("BNE"))
                                        pass2out.add(stn+"\t\t"+lc+"\t\t"+"BC"+"\t"+content);
                                    else
                                        pass2out.add(stn+"\t\t"+lc+"\t\t"+tokens[lk]+"\t"+content);
                                    //bt.put(mi,min);
                                }
                            }
                        }
                        else if(flag==false && tokens[lk].equals("BR")) {
                            String content="15,";
                            content+=data[0];
                            pass2out.add(stn+"\t\t"+lc+"\t\t"+"BCR"+"\t"+content+"\n");
                        }
                        lc+=mot.get(tokens[lk]);
                    }
                }
                else {
                    if(tokens[lk].equals("LTORG")) {
                        while(lc%8!=0)
                            lc++;
                        for(String s1:hp2.keySet()) {
                            //System.out.println(s1);
                            String temp="";
                            int in=-1;
                            //System.out.println(s1);
                            if(s1.contains("(")) {
                                in=s1.indexOf("(");
                                int in1 = s1.indexOf(")");
                                temp=s1.substring(in+1,in1);
                                //System.out.println(temp);
                            }
                            else if(s1.contains("'")) {
                                in=s1.indexOf("'");
                                int in1=s1.indexOf("'",in+1);
                                //System.out.println(in+" "+in1);
                                temp=s1.substring(in+1,in1);
                            }
                            //System.out.println(temp);
                            if(!temp.equals("") && !isInteger(temp)) {
                                String content=hp1.get(temp)+"\n";
                                //System.out.println(stn+"\t\t"+lc+"\t\t"+content);
                                pass2out.add(stn+"\t\t"+lc+"\t\t"+content);
                                lc+=4;
                            }
                            else if(!temp.equals("") && isInteger(temp)) {
                                pass2out.add(stn+"\t\t"+lc+"\t\t"+temp+"\n");
                                lc+=4;
                            }
                            stn++;
                        }
                    }
                    else if(tokens[lk].equals("DS")) {
                        String temp = hp1.get(tokens[lk-1]);
                        pass2out.add(stn+"\t\t"+temp+"\t\t.\n");
                    }
                    else if(tokens[lk].equals("DC")) {
                        String temp = hp1.get(tokens[lk-1]);
                        pass2out.add(stn+"\t\t"+temp+"\t\t25..\n");
                    }

                }
                stn++;
            }
        }

        for(String s1:pass2out) 
            System.out.println(s1);

    }

    public static int hasLiterals(String data[]) {

        int in=0;

        for(String temp:data) {
            if(temp.charAt(0)=='=')
                return in;
            in++;
        }
        return -1;
    }
    public static void library() {
        pot.add("START");
        pot.add("END");
        pot.add("DC");
        pot.add("DS");
        pot.add("EQU");
        pot.add("LTORG");

        mot.put("LA",4);
        mot.put("SR",2);
        mot.put("L",4);
        mot.put("AR",2);
        mot.put("A",4);
        mot.put("C",4);
        mot.put("BNE",4);
        mot.put("LR",2);
        mot.put("ST",4);
        mot.put("BR",2);
    }

    public static boolean isInteger(String str) {

        int in;
        try {
            in = Integer.parseInt(str);
        }
        catch(NumberFormatException e) {
            return false;
        }
        return true;
    }
}

