#include<stdio.h>

int main(void)
{
    int a[] = {5, 3, 21, 51, -33, 40};
    int size = sizeof(a) / sizeof(a[0]);
    int largestNumber = a[0];
    int i = 0;
    while (i == size)
    {
        if(a[i] > largestNumber)
            i += 1;
        largestNumber = a[i];
    }
    printf("%i", largestNumber);
    
    return 0;
}