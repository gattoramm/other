public class Bike {
    int gear;
    int speed;

    Bike(int gear, int speed) {
        this.gear = gear;
        this.speed = speed;
    }

    public String toString() {
        return "(" + gear + ", " + speed + ")";
    }

    public static void main(String[] args) {
        Bike honda = new Bike(3, 200);
        Bike ducati = new Bike(1, 15);

        System.out.println(honda);
        System.out.println(ducati);
    }
}