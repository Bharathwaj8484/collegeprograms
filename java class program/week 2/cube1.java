interface Shape {
    double calculateArea();
}

interface rec extends Shape {
double calper();
}

class cuboid implements rec {
    double len;
    double wth;
    double hei;

    public cuboid(double l, double w, double h) {
        len = l;
        wth = w;
        hei = h;
    }

    public double calculateArea() {
        return 2 * (len * wth + len * hei + wth * hei);
    }

    public double calper() {
        return 4 * (len + wth + hei);
    }

    public double calv() {
        return len * wth * hei;
    }
}

public class cube1 {
    public static void main(String[] args) {
        cuboid cuboid = new cuboid(3.0, 4.0, 5.0);

        double area = cuboid.calculateArea();
        double perimeter = cuboid.calper();
        double volume = cuboid.calv();

        System.out.println("cuboid Area: " + area);
        System.out.println("cuboid Perimeter: " + perimeter);
        System.out.println("cuboid Volume: " + volume);
    }
}
