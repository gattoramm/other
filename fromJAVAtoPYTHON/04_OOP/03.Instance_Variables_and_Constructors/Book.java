public class Book {
    String name;

    Book(String name) {
        this.name = name;
    }

    public String toString() {
        return name;
    }

    public static void main(String[] args) {
        Book book1 = new Book("John");
        Book book2 = new Book("Mike");

        System.out.println(book1);
        System.out.println(book2);
    }
}