// problem: https://www.hackerrank.com/challenges/staircase/problem


#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {
    int j = 0;
    for(int i = n-1; i >= 0; i--){
        for(j=0; j < i; j++){
            cout<<" ";
        }
        for(j = n-j; j>0; j--){
            cout<<"#";
        }
        cout << "\n";
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
