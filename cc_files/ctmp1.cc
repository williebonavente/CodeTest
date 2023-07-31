#include <algorithm> // For std::sort function
#include <cassert>   // For std::assert
#include <iostream>  // For IO operations
#include <vector>    // For std::vector

namespace search
{

    namespace binary_search
    {

        // Binary search algorithm to find the index of a value in a sorted vector
        uint64_t binarySearch(const std::vector<uint64_t> &arr, uint64_t val)
        {
            uint64_t low = 0;
            uint64_t high = arr.size() - 1;

            while (low <= high)
            {
                uint64_t mid = low + (high - low) / 2;

                if (val == arr[mid])
                {
                    return mid;
                }
                else if (val < arr[mid])
                {
                    high = mid - 1;
                }
                else
                {
                    low = mid + 1;
                }
            }
            return static_cast<uint64_t>(-1); // If val is not in the array, return -1.
        }

    } // namespace binary_search

} // namespace search

// Self-test implementation
void runTests()
{
    std::vector<uint64_t> arr1 = {1, 3, 5, 7, 9, 8, 6, 4, 2};
    std::sort(arr1.begin(), arr1.end());
    uint64_t expected_ans1 = 3;
    uint64_t derived_ans1 = search::binary_search::binarySearch(arr1, 4);
    std::cout << "Test #1: ";
    assert(derived_ans1 == expected_ans1);
    std::cout << "Passed!" << std::endl;

    std::vector<uint64_t> arr2 = {1, 23, 25, 4, 2};
    std::sort(arr2.begin(), arr2.end());
    uint64_t expected_ans2 = 4;
    uint64_t derived_ans2 = search::binary_search::binarySearch(arr2, 25);
    std::cout << "Test #2: ";
    assert(derived_ans2 == expected_ans2);
    std::cout << "Passed!" << std::endl;

    std::vector<uint64_t> arr3 = {1, 31, 231, 12, 12, 2, 5, 51, 21, 23, 12, 3};
    std::sort(arr3.begin(), arr3.end());
    uint64_t expected_ans3 = 8;
    uint64_t derived_ans3 = search::binary_search::binarySearch(arr3, 31);
    std::cout << "Test #3: ";
    assert(derived_ans3 == expected_ans3);
    std::cout << "Passed!" << std::endl;
}

int main()
{
    runTests();
    return 0;
}
