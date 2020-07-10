//problem: https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int i;
    long l;
    char c;
    float f;
    double lf;
    scanf("%i %ld %c %f %lf", &i, &l, &c, &f, &lf);
    printf("%i\n%ld\n%c\n%f\n%lf", i, l, c, f, lf);
    return 0;
}