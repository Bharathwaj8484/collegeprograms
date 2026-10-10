import java.util.*;
class methodover{
  public static void main(String[] args) {
	mol m=new mol();
	System.out.println(m.area(10));
	System.out.println(m.area(4.5f));
	System.out.println(m.area(10,4.5f));
	System.out.println(m.area(4.5f,10));
}
}

class mol{
int area(int x){
return x*x; }

float area(float x){
return x+x;}

float area(int x, float y){
return x+y; }

float area(float x,int y){
return x*y; }
}