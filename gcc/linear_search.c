// Online C compiler to run C program online
#include <stdio.h>

void linear_search(int arr[], int search, int);

int main()
{
    // Write C code here

    int arr[] = {1, 2, 3, 0, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    // Function call
    linear_search(arr, 3, size);

    return 0;
}


void linear_search(int arr[], int search, int n)
{
    int location = -1;

    int i = 0;

    while(i <= n && search != arr[i])
    {
        i = i + 1;
    }

    if (i <= n)
    {
        location = i;
        printf("Location %i", location);
    }
    else
        location = 0;

}