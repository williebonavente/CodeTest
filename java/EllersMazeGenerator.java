import java.util.*;

public class EllersMazeGenerator {
    public static void main(String[] args) {
        int rows = 10; // Number of rows in the maze
        int columns = 10; // Number of columns in the maze

        generateMaze(rows, columns);
    }

    public static void generateMaze(int rows, int columns) {
        int[][] grid = new int[rows][columns];
        int setNumber = 1;

        // Initialize the first row with distinct sets
        for (int i = 0; i < columns; i++) {
            grid[0][i] = setNumber++;
        }

        Random random = new Random();

        // Merge sets and create vertical connections
        for (int row = 1; row < rows; row++) {
            for (int col = 0; col < columns; col++) {
                // If not in the last column, randomly merge sets
                if (col < columns - 1 && random.nextBoolean()) {
                    grid[row][col + 1] = grid[row][col];
                }

                // Create vertical connections
                if (grid[row][col] == 0 || (col < columns - 1 && grid[row][col] != grid[row][col + 1])) {
                    grid[row][col] = setNumber++;
                }
            }

            // Merge sets in the same row
            ArrayList<Integer> rowSets = new ArrayList<>();
            for (int col = 0; col < columns; col++) {
                if (!rowSets.contains(grid[row][col])) {
                    rowSets.add(grid[row][col]);
                }
            }

            Collections.shuffle(rowSets, random);

            for (int col = 0; col < columns; col++) {
                grid[row][col] = rowSets.get(col);
            }
        }

        // Print the maze
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < columns; col++) {
                if (grid[row][col] == 0) {
                    System.out.print("█"); // Wall
                } else {
                    System.out.print(" "); // Path
                }
            }
            System.out.println();
        }
    }
}
