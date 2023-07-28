public class ctmp2 {

    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        // Fix the code.
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {

        int x;
        x = fibonacci(5);
        System.out.println(x);
    }

}