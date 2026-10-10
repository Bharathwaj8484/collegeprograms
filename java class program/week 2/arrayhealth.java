import java.util.Scanner;

public class arrayhealth {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int n = s.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = s.nextInt(); }
        String[] answer = processArray(arr);
        System.out.println("Processed array:");
        for (int i = 0; i < n; i++) {
            System.out.println("Answer[" + (i + 1) + "] = " + answer[i]);
}}
static String[] processArray(int[] arr) {
        String[] answer = new String[arr.length];
        for (int i = 0; i < arr.length; i++) {
        int num = arr[i];
        if (num % 3 == 0 && num % 5 == 0) {
        answer[i] = "health is wealth";
        } else if (num % 3 == 0) {
        answer[i] = "health";
        } else if (num % 5 == 0) {
        answer[i] = "wealth";
        } else {
         answer[i] = "zero";
            }
        }

        return answer;
    }
}
