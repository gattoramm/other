public class Book {
    String name;
    int copies;

    Book(String name, int copies) {
        this.name = name;
        this.copies = copies;
    }

    void increaseCopies(int howMuch) {
        this.copies += howMuch;
    }

    void decreaseCopies(int howMuch) {
        this.copies -= howMuch;
    }

    public String toString() {
        return "(" + name + ", " + copies + ")";
    }

    public static void main(String[] args) {
        Book book1 = new Book("John", 200);
        Book book2 = new Book("Mike", 15);

        System.out.println(book1);
        System.out.println(book2);
    }
}