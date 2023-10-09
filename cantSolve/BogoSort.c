#include <stdio.h>
#include <stdlib.h>

int isSorted(int *a, int n) {
    while (--n >= 1) {
        if (a[n] < a[n - 1]) {
            return 0;
        }
    }
    return 1;
}

void shuffle(int *a, int n) {
    int i, t, temp;
    for (i = 0;i < n;i++) {
        t = a[i];
        temp = rand() % n;
        a[i] = a[temp];
        a[temp] = t;
    }
}

void bogoSort(int *a, int n) {
    while (!isSorted(a, n)) {
        shuffle(a, n);
    }
}

int main() {
    int a[] = {5, 3, 2, 1, 4};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Unsorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    bogoSort(a, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    return 0;
}
