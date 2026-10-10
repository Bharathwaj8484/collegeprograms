import java.util.*;
class quiztest1 {
    public static void main(String[] args) {
	String ans="james gosling";
	Scanner s=new Scanner(System.in);
	int n=0;
	while(n<3){
		System.out.println("enter ans");
		String in= s.nextLine();
	
		if(in.equals(ans)){
			System.out.println("good");
			break; }
	
		else{
			System.out.println("try again"); }
	
		if (n==2){
		System.out.println("sorry,correct ans:james gosling"); }
		n++;
	}}}