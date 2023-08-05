#include <iostream>
#include <windows.h>

// Enum to represent console colors
enum ConsoleColor
{
    RED = BACKGROUND_RED,
    GREEN = BACKGROUND_GREEN,
    BLUE = BACKGROUND_BLUE,
    YELLOW = BACKGROUND_RED | BACKGROUND_GREEN,
    WHITE = BACKGROUND_RED | BACKGROUND_GREEN | BACKGROUND_BLUE,
};

// Function to set the console background color
void setConsoleColor(ConsoleColor color)
{
    CONSOLE_SCREEN_BUFFER_INFO consoleInfo;
    GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &consoleInfo);
    WORD attributes = consoleInfo.wAttributes;
    attributes &= ~(BACKGROUND_RED | BACKGROUND_GREEN | BACKGROUND_BLUE); // Clear existing background color
    attributes |= static_cast<WORD>(color); // Set new background color
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), attributes);
}

int main()
{
    int option;

    std::cout << "Welcome to Colorful Console!" << std::endl;

    while (true)
    {
        std::cout << "Select an option:" << std::endl;
        std::cout << "1. Red" << std::endl;
        std::cout << "2. Green" << std::endl;
        std::cout << "3. Blue" << std::endl;
        std::cout << "4. Yellow" << std::endl;
        std::cout << "5. Exit" << std::endl;

        std::cout << "Enter your choice: ";
        std::cin >> option;

        if (option == 1)
        {
            setConsoleColor(RED);
            std::cout << "You selected Red!" << std::endl;
            setConsoleColor(WHITE);
        }
        else if (option == 2)
        {
            setConsoleColor(GREEN);
            std::cout << "You selected Green!" << std::endl;
            setConsoleColor(WHITE);
        }
        else if (option == 3)
        {
            setConsoleColor(BLUE);
            std::cout << "You selected Blue!" << std::endl;
            setConsoleColor(WHITE);
        }
        else if (option == 4)
        {
            setConsoleColor(YELLOW);
            std::cout << "You selected Yellow!" << 1std::endl;
            setConsoleColor(WHITE);
        }
        else if (option == 5)
        {
            std::cout << "Goodbye!" << std::endl;
            break;
        }
        else
        {
            std::cout << "Invalid option. Please try again." << std::endl;
        }
    }

    return 0;
}
