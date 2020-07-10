//problem: https://www.hackerrank.com/challenges/variable-sized-arrays/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i, n, q, len, temp_int;
    vector<vector<int>> big_vec;
    vector<int> solutions;
    scanf("%i %i", &n, &q);
    for(i =0; i < n; i++){
        vector<int> temp_vec;
        cin>>len;
        for(int j = 0; j < len; j++){
            cin>>temp_int;
            temp_vec.push_back(temp_int);
        }
        big_vec.push_back(temp_vec);
    }
    int idx, pos;
    for(i = 0; i < q; i++){
        scanf("%i %i", &idx, &pos);
        solutions.push_back(big_vec[idx][pos]);
    }
    for(i=0; i < solutions.size(); i++){
        cout<<solutions[i]<<endl;
    }
    return 0;
}
