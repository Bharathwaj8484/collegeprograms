import java.util.Scanner;

public class Factor {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        System.out.print("Enter num ");
        int num = s.nextInt();
        System.out.print("Enter n ");
        int n = s.nextInt();
        System.out.println("Factors are ");
        for (int i = 1; i <= num; i++) {
        if (num % i == 0) {
        System.out.println(i); }}
        
	int c = 0,nth = 0;
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
            c++;
            if (c == n) {
            nth = i;
            break; 
	}}}
        if (nth != 0) {
            System.out.println("The " + n + "th factor of " + num + " is: " + nth);}
	else {
            System.out.println("The " + n + "th factor does not exist for " + num);
        }
    }
}
