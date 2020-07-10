//problem: https://www.hackerrank.com/challenges/vector-sort/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int i, amnt = 0, val = 0;
    vector<int> vec;
    cin >> amnt;
    for(i = 0; i < amnt; i++){
        cin >> val;
        vec.push_back(val);
    }
    sort(vec.begin(), vec.end());
    for(i = 0; i < vec.size(); i++){
        cout << vec[i] << " ";
    }
    return 0;
}
