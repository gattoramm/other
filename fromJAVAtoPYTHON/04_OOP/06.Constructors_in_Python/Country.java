public class Country {
    Country() {
        System.out.println("constructor1");
    }

    Country(String name) {
        System.out.println("constructor2");
    }

    void instance_method() {
        System.out.println("instance method");
    }
    public static void main(String[] args) {
        Country india1 = new Country();
        Country india2 = new Country("india");
        india1.instance_method();
    }
}