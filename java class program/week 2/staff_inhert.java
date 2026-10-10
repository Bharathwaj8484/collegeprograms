import java.util.*;
import java.io.*;
class staff_inhert {
  public static void main(String[] args) {
	casual o5=new casual();
	regular o4=new regular();
	officer o3=new officer();
	typist o2=new typist();
	teacher o1=new teacher();

	o5.d1();
	o1.d2();
	o2.d3();
	o3.d4();
	o4.d5();
	o5.d6();
  }
}
class staff {
	Scanner s=new Scanner(System.in);
	public void d1(){    
	System.out.println("enter name");
	String name = s.nextLine(); 
}
}
class teacher extends staff{
	public void d2(){    
	System.out.println("enter sub");
	String sub = s.nextLine();
	System.out.println("enter publication");
	String pub = s.nextLine();
}
}
class typist extends staff{
	public void d3(){    
	System.out.println("enter words per min");
	int word = s.nextInt();
}  
}
class officer extends staff{
	public void d4(){    
	System.out.println("enter grade");
	String g = s.nextLine();
}  
}

class regular extends typist{
	public void d5(){    
	System.out.println("enter salary");
	int sal = s.nextInt();
}  
}
class casual extends typist{
	public void d6(){    
	System.out.println("enter wages per day");
	int wage = s.nextInt();
}  
}



