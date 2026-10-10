import java.util.*;
class hybrid_inhert {
  public static void main(String[] args) {
	a obj= new a();
	d obj1= new d();
	obj1.display();
	obj1.display3();
	obj.display1();
	obj.display2();
  }
}
class c {
	public void display(){    
	System.out.println("main-c");}

  }
class b extends c{
	public void display1(){    
	System.out.println("derived c");}
}
class a extends b{
	public void display2(){    
	System.out.println("derived b");}
  
}
class d extends c{
	public void display3(){    
	System.out.println("derived from main");
}}


