#include <climits>
#include <iostream>
using namespace std;

// Function to find the Minimum number of coins required to get Sum S
int findMinCoins(int arr[], int n, int N)
{
    // dp[i] = no of coins required to get a total of i
    int dp[N + 1];

    // 0 coins are needed for 0 sum
    dp[0] = 0;

    for (int i = 1; i <= N; i++)
    {
        // Initialize minimum number of coins needed to infinity
        dp[i] = INT_MAX;
        int res = INT_MAX;

        // Iterate over each coin
        for (int c = 0; c < n; c++)
        {
            // Check if coins doesn't become negative by including it
            if (i - arr[c] >= 0)
                res = dp[i - arr[c]];

            // If the total can be reached by including the current coin 'c',
            // update the minimum number of coins needed dp[i]
            if (res != INT_MAX)
                dp[i] = min(dp[i], res + 1);
        }
    }

    // The Minimum No of Coins Required for N = dp[N]
    return dp[N];
}

int main()
{
    // No of Coins We Have
    int arr[] = {1, 2, 3, 4};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Total Change Required
    int N = 15;

    // Find the minimum number of coins required and print the result
    cout << "Minimum Number of Coins Required: " << findMinCoins(arr, n, N)
         << "\n";

    return 0;
}
