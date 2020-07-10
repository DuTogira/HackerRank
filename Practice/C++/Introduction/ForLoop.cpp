//problem: https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a, b;
    cin>>a;
    cin>>b;
    for(a; a <= b; a++){
        switch(a){
            case(1):
                printf("one\n");
                break;
            case(2):
                printf("two\n");
                break;
            case(3):
                printf("three\n");
                break;
            case(4):
                printf("four\n");
                break;
            case(5):
                printf("five\n");
                break;
            case(6):
                printf("six\n");
                break;
            case(7):
                printf("seven\n");
                break;
            case(8):
                printf("eight\n");
                break;
            case(9):
                printf("nine\n");
                break;
        }
        if(a > 9){
            if(a%2==0)
                printf("even\n");
            else
                printf("odd\n");
        }
    }
    return 0;
}
