import java.util.*;
import java.io.*;
class multi_inhert {
  public static void main(String[] args) {
	regular o4=new regular();
	typist o2=new typist();

	o4.d1();
	o2.d3();
	o4.d5();
	
  }
}
class staff {
	Scanner s=new Scanner(System.in);
	public void d1(){    
	System.out.println("enter name");
	String name = s.nextLine(); 
}
}

class typist extends staff{
	public void d3(){    
	System.out.println("enter words per min");
	int word = s.nextInt();
}  
}

class regular extends typist{
	public void d5(){    
	System.out.println("enter salary");
	int sal = s.nextInt();
}  
}




