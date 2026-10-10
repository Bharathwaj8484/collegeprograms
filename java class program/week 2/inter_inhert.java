import java.util.*;
class inter_inhert {
  public static void main(String[] args) {
	c3 obj= new c3();
	obj.display();
	obj.display2();
  }
}
class c1 {
	public void display(){    
	System.out.println("main");}

  }
interface c2 {
	public void display2();
}
class c3 extends c1 implements c2{
	public void display2(){    
	System.out.println("derived c3");}
  
}

