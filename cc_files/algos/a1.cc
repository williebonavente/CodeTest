#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

double median(std::vector<int>& nums) {
    // Sort the array in ascending order
    std::sort(nums.begin(), nums.end());
    size_t length = nums.size();
    size_t midIndex = length / 2;

    // Check if the array has odd or even length
    if (length % 2 == 0) {
        // For even length, take the average of the middle two elements
        return static_cast<double>(nums[midIndex] + nums[midIndex - 1]) / 2;
    } else {
        // For odd length, return the middle element
        return static_cast<double>(nums[midIndex]);
    }
}

int main() {
    // Read input from the user
    std::cout << "Enter the numbers separated by spaces: ";
    std::string inputLine;
    std::getline(std::cin, inputLine);

    std::vector<int> nums;
    std::istringstream iss(inputLine);
    int num;
    while (iss >> num) {
        nums.push_back(num);
    }

    // Calculate and display the median
    double result = median(nums);
    std::cout << "Median: " << result << std::endl;

    return 0;
}
