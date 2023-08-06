#include <iostream>
#include <windows.h>

/**
 * @enum OpponentColor
 * Enum to represent opponent color channels
 */
enum class OpponentColor
{
    RED_GREEN,
    BLUE_YELLOW,
    BLACK_WHITE
};

/**
 * @brief Set the console text color based on the opponent color channel
 * 
 * @param color The opponent color channel to set the text color
 */
void setConsoleColor(OpponentColor color)
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    switch (color)
    {
    case OpponentColor::RED_GREEN:
        SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_GREEN);
        break;
    case OpponentColor::BLUE_YELLOW:
        SetConsoleTextAttribute(hConsole, FOREGROUND_BLUE | FOREGROUND_GREEN);
        break;
    case OpponentColor::BLACK_WHITE:
        SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
        break;
    default:
        SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
    }
}

/**
 * @brief Clear the console screen
 */
void clearConsole()
{
    system("cls"); // Only works on Windows, for cross-platform support, consider using a cross-platform library
}

int main()
{
    std::cout << "Opponent-Process Theory Simulation" << std::endl;

    while (true)
    {
        // Clear the console screen between iterations
        clearConsole();

        // Display text with simulated opponent colors
        setConsoleColor(OpponentColor::RED_GREEN);
        std::cout << "Red-Green Channel" << std::endl;

        setConsoleColor(OpponentColor::BLUE_YELLOW);
        std::cout << "Blue-Yellow Channel" << std::endl;

        setConsoleColor(OpponentColor::BLACK_WHITE);
        std::cout << "Black-White Channel" << std::endl;

        setConsoleColor(OpponentColor::BLACK_WHITE); // Reset to default color
        std::cout << "Enter any key to continue or 'q' to quit: ";

        char input;
        std::cin >> input;
        if (input == 'q' || input == 'Q')
            break;
    }

    return 0;
}
