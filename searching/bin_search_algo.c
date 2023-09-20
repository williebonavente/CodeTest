#include <stdio.h>
#include "../src/DISP.H"

void binSearch(int arr[], int n, int target);

int main(void)
{
    int arr[5] = {1, 2, 3, 4, 5};
    binSearch(arr, 5, 3);
    displayArray(arr, 5);
    return 0;
}

void binSearch(int arr[], int n, int target)
{
    int i, j;
    i = 1;
    j = n;
    int temp;
    int location; // output
    while (i < j)
    {
        temp = (i + j) / 2;
        if (target > arr[temp])
            i = temp + 1;
        else
            j = temp;
    }
    if (target == arr[i])
    {
        location = i;
        printf("At index: %d", i);
    }
    else
    {
        location = -1;
        printf("Returning %d...Element not found\n", location);
    }
}