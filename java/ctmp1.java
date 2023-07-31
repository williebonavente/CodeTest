import java.util.Arrays;
import java.util.Scanner;

public class ctmp1 {
    private static final int[] examScores = {85, 78, 92, 95, 89, 80, 88, 93, 86, 91};
    private static final String PASSWORD = "secure123";

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the password to access the exam database: ");
            String inputPassword = scanner.nextLine();

            if (!inputPassword.equals(PASSWORD)) {
                System.out.println("Invalid password. Access denied.");
                return;
            }

            System.out.println("Access granted. The examination database is secure.");

            Arrays.sort(examScores); // The array must be sorted for binary search.

            System.out.print("Enter the student's ID to find their exam score: ");
            int targetID = scanner.nextInt();

            int index = binarySearch(targetID);
            if (index != -1) {
                int score = examScores[index];
                System.out.println("Student with ID " + targetID + " scored: " + score);
            } else {
                System.out.println("Student with ID " + targetID + " not found in the database.");
            }
        }
    }

    private static int binarySearch(int targetID) {
        int low = 0;
        int high = examScores.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            int midID = examScores[mid];

            if (midID == targetID) {
                return mid;
            } else if (midID < targetID) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return -1; // Not found
    }
}
