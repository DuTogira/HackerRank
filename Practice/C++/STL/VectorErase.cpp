//problem: https://www.hackerrank.com/challenges/vector-erase/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i, size = 0, base = 0, end = 0, pos = 0, temp = 0;
    vector<int> vec;
    cin >> size;
    for(i = 0; i < size; i++){
        cin >> temp;
        vec.push_back(temp);
    }
    cin >> pos;
    pos -= 1;
    cin >> base;
    base -= 1;
    cin >> end;
    end -= 1;
    vec.erase(vec.begin() + pos);
    vec.erase(vec.begin() + base, vec.begin() + end);
    cout << vec.size() << endl;
    for(i = 0; i < vec.size(); i++){
        cout << vec[i] << " ";
    }
    return 0;
}
