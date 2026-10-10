import java.util.Scanner;

public class empbonus {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the salary: ");
        double sal = s.nextDouble();
        System.out.print("Enter the grade (A or B): ");
        char g = s.next().charAt(0);
        if (sal < 10000) {
            sal += sal * 0.02;
        }
        double b = 0;
        if (g == 'A') {
            b = sal * 0.05;
        } else if (g == 'B') {
            b = sal * 0.10;
        }
        double t = sal + b;
        System.out.println("Bonus: $" + b);
        System.out.println("Total salary: $" + t);
    }
}
