#include <stdio.h>
#include <math.h>

// Function to calculate Karatsuba Multiplication
long karatsuba(long x, long y, int n) {
    if (n == 1) {
        return x * y;
    }

    int m = n / 2;
    long p = pow(10, m);

    long a = x / p;
    long b = x % p;
    long c = y / p;
    long d = y % p;

    long ac = karatsuba(a, c, m);
    long bd = karatsuba(b, d, m);
    long ad_bc = karatsuba(a + b, c + d, m) - ac - bd;

    return ac * pow(10, 2 * m) + ad_bc * pow(10, m) + bd;
}

int main() {
    long x = 1234;
    long y = 5678;

    int n = 4; // Number of digits in x and y

    long result = karatsuba(x, y, n);
    printf("Product: %ld\n", result);

    return 0;
}
