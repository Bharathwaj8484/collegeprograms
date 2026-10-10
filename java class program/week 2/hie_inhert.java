import java.util.*;
class hie_inhert {
  public static void main(String[] args) {
	c4 obj1=new c4();
	obj1.display();
	obj1.display4();
	c3 obj= new c3();
	obj.display1();
	obj.display2();
  }
}
class c1 {
	public void display(){    
	System.out.println("main");}

  }
class c2 extends c1{
	public void display1(){    
	System.out.println("derived c2");}
}
class c3 extends c2{
	public void display2(){    
	System.out.println("derived c3");}
  
}
class c4 extends c1{
	public void display4(){    
	System.out.println("derived from main");}
}

