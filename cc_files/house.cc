#include <iostream>
int main() {
    for (int i = 1; i <= 23; i++) {
        for (int j = 1; j <= 40; j++) {
            if (i >= 1 && i <= 11) {
                if (i == 1 && j >= 11 && j <= 30) {
                    std::cout << "-";
                }
                else if (i > 1 && (12 - i) == j) {
                    std::cout << "/";
                }
                else if (i > 1 && (29 + i) == j) {
                    std::cout << "\\";
                }
                else if (i <= 11 && (10 + i) == j) {
                    std::cout << "\\";
                }
                else if ((12 - i) <= j && (10 + i) >= j) {
                    std::cout << "S";
                }
                else if ((10 + i) <= j && (29 + i) >= j) {
                    std::cout << "Y";
                }
                else {
                    std::cout << " ";
                }
            }
            else if (i <= 16) {
                if (j == 1 || j == 21 || j == 40) {
                    std::cout << "|";
                }
                else {
                    std::cout << "#";
                }
            }
            else {
                if (j == 1 || j == 21 || j == 40) {
                    std::cout << "|";
                }
                else if (j <= 6 || (j >= 15 && j <= 21)) {
                    std::cout << "@";
                }
                else if (j == 7 || j == 14) {
                    std::cout << "|";
                }
                else if (j == 22 || j == 39) {
                    std::cout << "@";
                }
                else if (i <= 20) {
                    if (j == 23 || j == 38) {
                        std::cout << "|";
                    }
                    else {
                        std::cout << " ";
                    }
                }
                else {
                    if (j >= 23 && j <= 38) {
                        std::cout << "@";
                    }
                    else {
                        std::cout << " ";
                    }
                }
            }
        }
        std::cout << std::endl;
    }
    return 0;
}