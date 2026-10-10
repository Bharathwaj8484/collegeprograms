import java.util.*;
class inhert2 {
  public static void main(String[] args) {
    Scanner s=new Scanner(System.in);
    System.out.println("enter balance");
    int b= s.nextInt();
	
    master obj=new master();
	obj.display();
	obj.display1();
	obj.display2();
 	obj.display3(b);
}
}
class person {
	public void display(){    
	System.out.println("name: joe");}

  }
class account extends person{
	public void display1(){    
	System.out.println("account no:2H31KS2");}
}
class admin extends account{
	public void display2(){    
	System.out.println("admin ID: ASDE3413 ");}
  
}
class master extends admin{
	public void display3(int x){    
	System.out.println("balance "+x);}
}

