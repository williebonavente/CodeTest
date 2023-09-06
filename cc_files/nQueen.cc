#include <iostream>
#include <vector>
#include <string>

bool isSafe(
    int row,
    int col,
    const std::vector<int>& left_diagonal,
    const std::vector<int>& right_diagonal,
    const std::vector<int>& vertical
) {
    return (left_diagonal[row + col] == 0 &&
            right_diagonal[row - col + right_diagonal.size() - 1] == 0 &&
            vertical[col] == 0);
}

void depthFirstSearch(
    std::vector<std::vector<std::string>>& boards,
    std::vector<std::string>& board,
    const std::vector<int>& left_diagonal,
    const std::vector<int>& right_diagonal,
    const std::vector<int>& vertical,
    int row,
    int n
) {
    if (row == n) {
        boards.push_back(board);
        return;
    }

    for (int col = 0; col < n; col++) {
        if (isSafe(row, col, left_diagonal, right_diagonal, vertical)) {
            std::vector<int> new_left_diagonal = left_diagonal;
            std::vector<int> new_right_diagonal = right_diagonal;
            std::vector<int> new_vertical = vertical;

            new_left_diagonal[row + col] = 1;
            new_right_diagonal[row - col + right_diagonal.size() - 1] = 1;
            new_vertical[col] = 1;
            board[row][col] = 'Q';

            depthFirstSearch(boards, board, new_left_diagonal, new_right_diagonal, new_vertical, row + 1, n);

            board[row][col] = '.';
        }
    }
}

void nQueensSolution(int n) {
    std::vector<std::vector<std::string>> boards;
    std::vector<std::string> board(n, std::string(n, '.'));

    // Vectors to keep track of occupied diagonals and vertical positions
    std::vector<int> left_diagonal(2 * n - 1, 0);
    std::vector<int> right_diagonal(2 * n - 1, 0);
    std::vector<int> vertical(n, 0);

    depthFirstSearch(boards, board, left_diagonal, right_diagonal, vertical, 0, n);

    // Print all the boards
    for (const auto& board : boards) {
        for (const auto& row : board) {
            std::cout << row << std::endl;
        }
        std::cout << std::endl;
    }

    std::cout << boards.size() << " solutions were found." << std::endl;
}

int main() {
    nQueensSolution(4);
    return 0;
}
