import java.util.concurrent.*;
class thread1{
public static void main(String[] args){
	new A().start();
	new B().start();
	new C().start();
}}

class A extends Thread
{
public void run()
{
	for(int i=0;i<5;i++){
	if(i==3){
		sleep(550);}
	else{
		System.out.println(i);}}}}
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

	