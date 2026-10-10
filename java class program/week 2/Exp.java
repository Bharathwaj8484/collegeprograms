class own extends Exception {
    own(String msg) {
        super(msg);
    }
}
class Exp {
    public static void main(String[] args) {
        int x = 2, z, y = 10000;
        try {
         z = x / y;
            if (z > 0.001) {
            throw new own("Number is small"); 
            }
   } catch (own e) {
            System.out.println(e.getMessage());
}}}
