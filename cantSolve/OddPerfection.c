#include <stdio.h>
#include <stdbool.h>

// Function to check if a number is perfect
bool is_perfect(int n) {
    int sum = 1;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            sum += i;
            if (i != n / i) {
                sum += n / i;
            }
        }
    }
    return sum == n;
}

int main() {
    int limit;

    // Input the limit for searching
    printf("Enter the limit for searching odd perfect numbers: ");
    scanf("%d", &limit);

    if (limit <= 0) {
        printf("Invalid limit.\n");
        return 1;
    }

    printf("Searching for odd perfect numbers up to %d...\n", limit);
    for (int n = 1; n <= limit; n += 2) {
        if (is_perfect(n)) {
            printf("Odd perfect number found: %d\n", n);
        }
    }

    printf("Search complete.\n");

    return 0;
}
