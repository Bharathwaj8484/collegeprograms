import java.util.concurrent.*;
class ThreadPrio{
public static void main(String[] args){
	A a=new A();
	a.start();
	new B().start();
	new C().start();
	a.setPriority(10);
}}

class A extends Thread
{
public void run()
{
	for(int i=0;i<5;i++){
	System.out.println(i);}}}
class B extends Thread
{
public void run()
{
	for(int j=10;j<15;j++){
	System.out.println(j);}}}
class C extends Thread
{
public void run()
{
	for(int k=20;k<25;k++){
	System.out.println(k);}}}

	