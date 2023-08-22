#include <stdio.h>

int main(void)
{
    int n; // size 
    int f = 1;
    printf("Enter number >> ");
    scanf("%d", &n);
    int i;
    for (i = 1; i <= n; i++)
        f *= i;

    printf("%d", f);
    return 0;
}

