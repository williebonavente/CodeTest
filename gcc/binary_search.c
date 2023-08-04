#include <stdio.h>

int binary_search(int arr[], int search, int n);
int main(void)
{

    int arr[] = {1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 22};
    int size = sizeof(arr) / sizeof(arr[0]);
    int location, search;

    // Display the array
    printf("The list: "); 
    for (int i = 0; i < size; i++)
        printf("%i ", arr[i]);
    printf("\nEnter the number to search: ");
    scanf("%i", &search);

    // Function call
    location = binary_search(arr, search, size);

    printf("Location: %ith place", location + 1);

    return 0;
}

int binary_search(int arr[], int search, int n)
{
    int i, j, temp;
    int location;
    j = n;
    while (i < j)
    {
        temp = (i + j) / 2;
        if (search > arr[temp])
            i = temp + 1;
        else
            j = temp;
    }

    if (search == arr[i])
        location = i;
    else
        location = 0;

    return location;
}