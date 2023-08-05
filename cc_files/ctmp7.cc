#include <iostream>
#include <string>

std::string reverse_string(const std::string& str) {
    std::string reversed_str;
    for (int i = str.length() - 1; i >= 0; i--) {
        reversed_str.push_back(str[i]);
    }
    return reversed_str;
}

int main() {
    std::string input_string = "Hello Willie";
    std::string reversed_string = reverse_string(input_string);
    std::cout << "Reversed string: " << reversed_string << std::endl;
    return 0;
}
