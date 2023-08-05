#include <stdio.h>

void bubble_sort(int arr[], int size);
void display_arr(int arr[], int size);

int main(void)
{

    int arr[] = {3, 2, 4, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    bubble_sort(arr, n);
    display_arr(arr, n);

    return 0;
}

void bubble_sort(int arr[], int size)
{
    int i, j; // indexing variable
    int temp; // placeholder

    for (i = 0; i < size - 1; i++)
    {
        for (j = 0; j < size - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                // Swapping
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void display_arr(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%i ", arr[i]);
}