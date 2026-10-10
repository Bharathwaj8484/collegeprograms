import java.util.*;

public class days {
    public static void main(String[] args) {
    Scanner s = new Scanner(System.in);

    System.out.print("Enter number of days: ");
    int total = s.nextInt();

    int years = total / 365;
    int remain = total % 365;
    int weeks = remain / 7;
    int days = remain % 7;

    System.out.println("Years: " + years);
    System.out.println("Weeks: " + weeks);
    System.out.println("Days: " + days);
    }
}
