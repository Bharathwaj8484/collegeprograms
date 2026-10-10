import java.util.Scanner;

class Fruits {
    protected int count;

public Fruits() {
    count = 0; }

public void addb(int num) {
     count += num;}

public int getCount() {
     return count;}
}

class Apple extends Fruits {
public void adda(int num) {
addb(num);
}}

class Mango extends Fruits {
public void adda(int num) {
addb(num);}
}

public class basket1 {
public static void main(String[] args) {
    Scanner s = new Scanner(System.in);

    Apple apples = new Apple();
    Mango mangoes = new Mango();

    System.out.print("Enter number of apples ");
    int numa = s.nextInt();
    apples.adda(numa);

    System.out.print("Enter number of mangoes ");
    int numm = s.nextInt();
    mangoes.adda(numm);

    System.out.println("Number of apples: " + apples.getCount());
    System.out.println("Number of mangoes: " + mangoes.getCount());

    int totalFruits = apples.getCount() + mangoes.getCount();
    System.out.println("Total number of fruits in the basket: " + totalFruits);
    }
}
