import java.util.Scanner;

public class PerfectNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Given Number: ");
        int number = sc.nextInt();
        sc.close();

        if (number < 1) {
            System.out.println("Please enter a positive integer.");
        } else {
            int sum = 0;
            for (int i = 1; i <= number / 2; i++) {
                if (number % i == 0) {
                    sum += i;
                }
            }

            if (sum == number) {
                System.out.println("It's a Perfect Number");
            } else {
                System.out.println("It's not a Perfect Number");
            }
        }
    }
}
