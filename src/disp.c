#include <stdio.h>
#include "disp.h" // include the header file 

// Implementing the function to display the elements of an array
void displayArray(int arr[], int size)
{
    int i;
    for(int i = 0; i < size; i++)
        printf(" %d",arr[i]);
}