#include <stdio.h>
#include <math.h>

int main() {
    double x;
    double result;

    printf("Enter the value of x: ");
    scanf("%lf", &x);

    // Calculate the expression
    result = (3 * pow(x + 2, 2) * pow(x - 3, 2) - (x + 2) * (x + 2) * 2 * (x - 3)) / pow(x - 3, 4);

    printf("Result: %lf\n", result);

    return 0;
}
