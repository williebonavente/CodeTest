#include <stdio.h>
#include <stdbool.h>

// Function to check if a number is prime
bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    int range_start, range_end;

    // Input the range
    printf("Enter the starting and ending values of the range: ");
    scanf("%d %d", &range_start, &range_end);

    if (range_start >= range_end) {
        printf("Invalid range.\n");
        return 1;
    }

    // Find twin primes in the specified range
    printf("Twin primes in the range %d to %d:\n", range_start, range_end);
    for (int n = range_start; n <= range_end - 2; n++) {
        if (is_prime(n) && is_prime(n + 2)) {
            printf("(%d, %d)\n", n, n + 2);
        }
    }

    return 0;
}
