#include <stdio.h>
#include <math.h>
#include "main.h"
void solve_quadratic(float a, float b, float c) {
	/* Calculate the discriminant */

       	float x, discriminant;

    // Calculate the discriminant
    discriminant = b*b - 4*a*c;

    // Check if the discriminant is positive, negative, or zero
    if (discriminant > 0) {
        // Two real roots
        x = (-b + sqrt(discriminant)) / (2*a);
         printf("x = %.2f \n", x);
        x= (-b - sqrt(discriminant)) / (2*a);
        printf("x = %.2f\n", x);
    } else if (discriminant == 0) {
        // One real root
        x = -b / (2*a);
        printf("x  = %.2f\n", x);
    } else {
        // No real roots (complex roots)
        float real_part = -b / (2*a);
        float imaginary_part = sqrt(-discriminant) / (2*a);
        printf("x = %.2f + %.2fi and x = %.2f - %.2fi\n", real_part, imaginary_part, real_part, imaginary_part);
    }
}

