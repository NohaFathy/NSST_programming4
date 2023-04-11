#include<stdio.h>
#include"main.h"

int main() {
    float a, b, c;

    printf("Enter the values of a, b, and c: ");
    scanf("%f %f %f", &a, &b, &c);

    solve_quadratic(a, b, c);

    return 0;
}
