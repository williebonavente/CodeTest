#include <stdio.h>
#include <stdbool.h>

// Function to check if a number is prime
bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

// Function to find two prime numbers that sum up to n (Goldbach Conjecture)
void goldbachConjecture(int n) {
    if (n <= 2 || n % 2 != 0) {
        printf("Goldbach Conjecture is only applicable to even numbers greater than 2.\n");
        return;
    }
    for (int i = 2; i <= n / 2; i++) {
        if (isPrime(i) && isPrime(n - i)) {
            printf("%d = %d + %d\n", n, i, n - i);
            return;
        }
    }
    printf("Goldbach Conjecture is false for %d!\n", n);
}

int main() {
    int limit;
    
    printf("Enter the limit for even numbers (greater than 2): ");
    scanf("%d", &limit);
    
    if (limit <= 2 || limit % 2 != 0) {
        printf("Invalid input. Please enter an even number greater than 2.\n");
        return 1;
    }
    
    for (int i = 4; i <= limit; i += 2) {
        goldbachConjecture(i);
    }
    
    return 0;
}
