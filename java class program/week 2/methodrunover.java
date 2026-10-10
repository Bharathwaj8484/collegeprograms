import java.util.*;
class methodrunover {
  public static void main(String[] args) {
	B obj=new B();
	A obj1=new A();
	obj1.display();
	obj.display();
	
  }
}
class A {
	public void display(){    
	System.out.println("main");}

  }
class B extends A{
	public void display(){    
	System.out.println("derived");}
}



