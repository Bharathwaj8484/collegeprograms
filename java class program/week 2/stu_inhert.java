import java.util.*;
import java.io.*;
class stu_inhert {
  public static void main(String[] args) {
	result o=new result();
	o.d1();
	o.d3();
	o.d5();
	
  }
}
class stu {
	public void d1(){    
	System.out.println("roll no: 1922334"); 
}
}

class test extends stu{
	public void d3(){    
	System.out.println("marks of five sub \n86\n89\n90\n92\n98");
}  
}

class result extends test{
	public void d5(){    
	System.out.println("enter result: 445");
}  
}




