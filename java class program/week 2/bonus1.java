import java.util.Scanner;

class Employee {
    protected String name;
    protected double salary;

public Employee() {
    name = "";
    salary = 0.0;}

public void getData() {
    Scanner s = new Scanner(System.in);
    System.out.print("Enter employee name: ");
    name = s.nextLine();
    System.out.print("Enter employee salary: ");
    salary = s.nextDouble();
}

public void display() {
    System.out.println("Employee Name: " + name);
    System.out.println("Employee Salary: " + salary);
}

public double calub() {
     return 0.0;
    }
}

class admin extends Employee {
    
public double calub() {
    return salary * 0.1;
    }
}

class acc extends Employee {
   
public double calub() {
    return salary * 0.08;
    }
}

public class bonus1 {
 public static void main(String[] args) {
    Scanner s = new Scanner(System.in);

    System.out.println("Select Employee Type:");
     System.out.println("1. admin");
    System.out.println("2. Account");
    int choice = s.nextInt();
    Employee employee;

        if (choice == 1) {
            employee = new admin();
        } else {
            employee = new acc();
        }

employee.getData();
employee.display();
double bonus = employee.calub();
System.out.println("Bonus: " + bonus);}
}
