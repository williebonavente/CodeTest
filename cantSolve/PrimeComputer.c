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
    int limit;

    // Input the limit
    printf("Enter the upper limit to find prime numbers: ");
    scanf("%d", &limit);

    if (limit <= 1) {
        printf("Invalid limit. Please enter a positive integer greater than 1.\n");
        return 1;
    }

    // Find and print prime numbers up to the limit
    printf("Prime numbers up to %d:\n", limit);
    for (int n = 2; n <= limit; n++) {
        if (is_prime(n)) {
            printf("%d ", n);
        }
    }
    printf("\n");

    return 0;
}
