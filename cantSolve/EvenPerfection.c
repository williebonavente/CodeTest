#include <stdio.h>
#include <stdint.h>
#include <math.h>

// Function to check if a number is prime (naive method)
int is_prime(uint64_t n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    for (uint64_t i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return 0;
    }
    return 1;
}

// Function to check if 2^p - 1 is prime (Mersenne prime)
int is_mersenne_prime(int p) {
    uint64_t mersenne = pow(2, p) - 1;
    return is_prime(mersenne);
}

int main() {
    int p = 2; // Starting with p = 2 for 2^p - 1
    int count = 0; // Count of even perfect numbers found

    printf("Even Perfect Numbers (2^p - 1) that are Mersenne primes:\n");

    while (1) {
        if (is_mersenne_prime(p)) {
            uint64_t even_perfect = pow(2, p - 1) * (pow(2, p) - 1);
            printf("2^%d - 1 = %llu (Even Perfect: %llu)\n", p, (unsigned long long)(pow(2, p) - 1), even_perfect);
            count++;
        }

        // Stop after finding a certain number of even perfect numbers
        if (count >= 5) {
            break;
        }

        p++;
    }

    return 0;
}
