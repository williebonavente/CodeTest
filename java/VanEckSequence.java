public class VanEckSequence {
    public static void main(String[] args) {
        int n = 30; // Change this value to generate more or fewer terms
        int[] sequence = new int[n];

        sequence[0] = 0; // The first term is always 0

        for (int i = 1; i < n; i++) {
            int previous = sequence[i - 1];
            int j;

            for (j = i - 2; j >= 0; j--) {
                if (sequence[j] == previous) {
                    break;
                }
            }

            if (j >= 0) {
                sequence[i] = i - j;
            } else {
                sequence[i] = 0;
            }
        }

        // Print the sequence
        for (int i = 0; i < n; i++) {
            System.out.print(sequence[i] + " ");
        }
    }
}
