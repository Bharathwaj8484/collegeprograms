public class TryCatch {
    public static void main(String[] args) {
        int[] numbers = { 1, 2, 3, 4, 5 };
        
        try {
  
            int result = numbers[10];
            System.out.println("Element at index 10: " + result);
        } catch (ArrayIndexOutOfBoundsException e) {
      
            System.out.println("Exception caught: " + e.getMessage());
        }
       
    }
}
