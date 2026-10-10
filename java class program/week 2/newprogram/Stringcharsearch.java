public class Stringcharsearch {
    public static void main(String args[]){
        String a="Engineering";
        char s='r';
        if (a.contains(s+"")==true)
            System.out.println(a.indexOf(s));
        else
            System.out.println("not");
    }    
}
