#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator with the current time
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    int secretNumber = std::rand() % 100 + 1; // Generate a random number between 1 and 100
    int guess;
    int attempts = 0;

    std::cout << "Welcome to Guess the Number Game!" << std::endl;
    std::cout << "I have a secret number between 1 and 100. Can you guess it?" << std::endl;

    while (true) {
        std::cout << "Enter your guess: ";
        std::cin >> guess;

        attempts++;

        if (guess == secretNumber) {
            std::cout << "Congratulations! You guessed the correct number " << secretNumber << " in " << attempts << " attempts." << std::endl;
            break;
        } else if (guess < secretNumber) {
            std::cout << "Too low. Try again." << std::endl;
        } else {
            std::cout << "Too high. Try again." << std::endl;
        }
    }

    return 0;
}
