//problem: https://www.hackerrank.com/challenges/c-tutorial-functions/problem

#include <iostream>
#include <cstdio>
using namespace std;

#define SIZE 4

int max_of_four(int a, int b, int c, int d){
    int arr[SIZE] = {a, b, c, d};
    int max = 0;
    for(int i =0; i < SIZE; i++){
        if(arr[i] > max)
            max = arr[i];
    }
    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
