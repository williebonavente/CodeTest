#include <stdio.h>

void binSearch(int arr[], int n, int target);


int main(void)
{   
    
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
        if(target > arr[temp]) i = temp + 1;
        else j = temp;
    }
    if(target == arr[i]) location = i;
    else location = -1;
}