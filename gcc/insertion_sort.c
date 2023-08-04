#include <stdio.h>

void insertion_sort(int arr[], int size);
void display_list(int arr[], int size);

int main(void)
{

    int arr[] = {3, 2, 1, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    insertion_sort(arr, n);
    display_list(arr, n);
    return 0;
}

void insertion_sort(int arr[], int size)
{
    int i, j, k, temp;

    for (j = 1; j < size; j++)
    {
        i = j - 1;
        while (i >= 0 && arr[j] < arr[i])
            i -= 1;

        temp = arr[j];

        for (k = j; k > i + 1; k--)
        {
            arr[k] = arr[k - 1];
        }

        arr[i + 1] = temp;
    }
}

void display_list(int arr[], int size)
{
    int z;
    for (z = 0; z < size; z++)
    {
        printf("%i ", arr[z]);
    }
}