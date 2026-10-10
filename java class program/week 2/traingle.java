import java.util.*;

class traingle {
    public static void main(String[] args) {
        double s1 = 13;
        double s2 = 13;
        double s3 = 13;

if ((s1 != s2) && (s2 != s3) && (s1 != s3)) {
System.out.println("Is Scalene: true"); } 
else {
    System.out.println("Is Scalene: false");
        }

if ((s1 == s2) || (s2 == s3) || (s1 == s3)) {
     System.out.println("Is Isosceles: true");
} else {
     System.out.println("Is Isosceles: false");
}

 if ((s1 == s2) && (s2 == s3)) {
    System.out.println("Is Equilateral: true"); }
else {
    System.out.println("Is Equilateral: false");
 }


double[] sides = { s1, s2, s3 };
double maxs = Math.max(s1, Math.max(s2, s3));
int maxin = 0;
    for (int i = 0; i < 3; i++) {
    if (sides[i] == maxs) {
    maxin = i;
    break;}}

boolean right = false;
    if (maxin != 0) {
    double sum = 0;
    for (int i = 0; i < 3; i++) {
    if (i != maxin) {
    sum += sides[i] * sides[i]; }}
    right = (maxs * maxs == sum);
    System.out.println("Is Right: " + right);
    }
}
}