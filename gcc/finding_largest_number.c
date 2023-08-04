#include <stdio.h>

void findLargestNumber(int arr[], int n);

int main(void)
{

    int arr[] = {1, 5, 3, 4, 2};
    int size; // size of the array
    size = sizeof(arr) / sizeof(arr[0]);
    printf("The list: "); 
    for (int i = 0; i < size; i++)
        printf("%i ", arr[i]);

    findLargestNumber(arr, size);

    return 0;
}

void findLargestNumber(int arr[], int n)
{
    int temp;
    temp = arr[0];
    int i;
    for (i = 0; i < n; i++)
    {
        if (temp < arr[i])
            temp = arr[i];
    }

    printf("\nLargest number: %i", temp);
}