import java.util.Scanner;

public class perfectrange {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter range ");
        int range = s.nextInt();
        System.out.println("Perfect square numbers\n");
        for (int i = 1; i <= range; i++) {
        int sqrt = (int) Math.sqrt(i);
        if (sqrt * sqrt == i) {
        System.out.println(i);
        }}
        int sum = 0;
        for (int i = 1; i < 10; i++) {
        int sqrt = (int) Math.sqrt(i);
        if (sqrt * sqrt == i) {
        sum += i;
}}
        System.out.println("Sum less than 100: " + sum);
}}
