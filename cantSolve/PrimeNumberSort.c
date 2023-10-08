#include <stdio.h>
#include <stdbool.h>

// Function to generate prime numbers up to a given limit
void generatePrimes(int limit, bool isPrime[]) {
    for (int i = 2; i <= limit; i++) {
        isPrime[i] = true;
    }

    for (int p = 2; p * p <= limit; p++) {
        if (isPrime[p] == true) {
            for (int i = p * p; i <= limit; i += p) {
                isPrime[i] = false;
            }
        }
    }
}

// Function to perform Prime Number Sort using Bubble Sort
void primeNumberSort(int arr[], int n, int primeKeys[]) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (primeKeys[j] > primeKeys[j + 1]) {
                // Swap elements in the array
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                // Swap corresponding prime keys
                temp = primeKeys[j];
                primeKeys[j] = primeKeys[j + 1];
                primeKeys[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {5, 11, 7, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Define a limit for prime number generation
    int limit = 20;
    bool isPrime[limit + 1];
    generatePrimes(limit, isPrime);

    // Assign prime number keys to elements
    int primeKeys[n];
    for (int i = 0; i < n; i++) {
        primeKeys[i] = arr[i];
    }

    // Perform Prime Number Sort
    primeNumberSort(arr, n, primeKeys);

    // Print the sorted array
    printf("Sorted Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
