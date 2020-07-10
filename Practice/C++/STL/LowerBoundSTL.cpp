//problem: https://www.hackerrank.com/challenges/cpp-lower-bound/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i, size, temp, numq, q;
    vector<int> v;
    vector<int>::iterator iter;
    cin >> size;
    for(i = 0; i < size; i++){
        cin >> temp;
        v.push_back(temp);
    }
    cin >> numq;
    for(i = 0; i < numq; i++){
        cin >> q;
        iter = lower_bound(v.begin(), v.end(), q);
        if(v[iter-v.begin()] == q)
            cout << "Yes ";
        else
            cout << "No ";
        cout << iter-v.begin() + 1 << endl;
    } 
    return 0;
}
