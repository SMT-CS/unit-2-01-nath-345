//
// Created by: Nathan
// Created on: Sep 2020
// This program calculates the area of a circle
//    with radius 15mm

#include <stdio.h>
#include <math.h>

int main()
{
    // this function calculates the area of a circle

    printf("If a circle has a radius of 15 mm: \n");
    printf("\n");
    printf("Area is %.2f mm².\n", (M_PI * pow(15, 2)));

    printf("\nDone.\n");
    return 0;
}