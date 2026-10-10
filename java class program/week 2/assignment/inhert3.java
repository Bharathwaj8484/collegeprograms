import java.util.*;
class inhert3 {
  public static void main(String[] args) {
	Scanner s=new Scanner(System.in);
	System.out.println("enter balance");
	int b = s.nextInt();	
	grandson obj=new grandson();
	obj.display(b);
	obj.display1(b);
}
}
class grandfather {
	public void display(int x){    
	System.out.println("grandafather property:"+x);}
	
 }
class grandson extends grandfather{
	public void display1(int x){    
	System.out.println("property grandson owns now: "+x);}
}


