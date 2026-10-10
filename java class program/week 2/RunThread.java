import java.util.concurrent.*;
class RunThread{
public static void main(String[] args){
	A a=new A();
	Thread t=new Thread(a);	
	t.start();	
}}


class A implements Runnable
{
public void run()
{
	for(int j=10;j<15;j++){
	System.out.println(j);}}}

	