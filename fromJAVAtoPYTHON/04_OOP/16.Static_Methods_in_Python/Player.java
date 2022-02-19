public class Player {
    private String name;
    private static int count;

    public Player(String name) {
        System.out.println("Player Constructor");
        this.name = name;
        count++;
    }

    public static int getCount() {
        return count;
    }

    public String getName() {
        return this.name;
    }
}
