#include <iostream>

using namespace std;

// Function to calculate binary exponentiation (a ^ n) % mod
long long binary_exponentiation(long long a, long long n, long long mod)
{
    long long result = 1;

    while (n > 0)
    {
        if (n % 2 == 1)
            result = (result * a) % mod;
        a = (a * a) % mod;
        n /= 2;
    }

    return result;
}

// Function to check if (a / b) % p equals a * (b ^ (p - 2)) % p
bool fermat_little_theorem(long long a, long long b, long long p)
{
    // Ensure p is a prime number, b divides a, and p doesn't divide b
    if (p <= 1 || b <= 0 || b >= p || a % b != 0)
        return false;

    // Using binary exponentiation method, O(log(p))
    long long result1 = (a / b) % p;
    long long result2 = (a * binary_exponentiation(b, p - 2, p)) % p;

    return result1 == result2;
}

int main()
{
    // A prime number
    long long p = 701;

    long long a = 1000000000;
    long long b = 10;

    // Using Fermat's Little Theorem to check if (a / b) % p equals a * (b ^ (p - 2)) % p
    if (fermat_little_theorem(a, b, p))
        cout << "(a / b) % p equals a * (b ^ (p - 2)) % p" << endl;
    else
        cout << "(a / b) % p does not equal a * (b ^ (p - 2)) % p" << endl;

    return 0;
}
