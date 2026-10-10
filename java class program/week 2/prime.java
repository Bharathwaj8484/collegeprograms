import java.util.Scanner;

public class prime {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = s.nextInt();
        if (isPrime(num)) {
            System.out.println(num + " prime number"); } 
	else {
            System.out.println(num + " not prime number"); }
        System.out.print("Enter n ");
        int n = s.nextInt();
        
        int c = 0;
        int current = 2; 
        while (c < n) {
            if (isPrime(current)) {
                c++;
                if (c== n) {
                System.out.println("The " + n + "th prime number is: " + current);
                break; }}
         current++;
        }}
    
    static boolean isPrime(int num) {
    if (num <= 1) {
    return false;}
        
     for (int i = 2; i * i <= num; i++) {
     if (num % i == 0) {
            return false; }}
        return true;
}}
