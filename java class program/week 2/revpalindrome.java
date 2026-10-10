import java.util.Scanner;

public class revpalindrome {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Enter number: ");
        int num = s.nextInt();
        int og = num;
        int r = 0;
        while (num != 0) {
            int d = num % 10;
            r = r * 10 + d;
            num /= 10;}
        int sum = og + r;
        System.out.println("Reverse: " + r);
        System.out.println("Sum: " + sum);
	int rev = 0;
	int tsum = sum;	
        while (tsum != 0) {
            int d = tsum % 10;
            rev = rev * 10 + d;
            tsum /= 10; }
	if (sum == rev) {
            System.out.println("The sum is a palindrome."); } 
	else {
            System.out.println("The sum is not a palindrome.");
        }}}


