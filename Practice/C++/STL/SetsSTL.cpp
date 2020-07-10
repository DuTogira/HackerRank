// Problem: https://www.hackerrank.com/challenges/cpp-sets/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i, numq, qtype, qval;
    set<int>s;
    set<int>::iterator iter;
    cin >> numq;
    for(i = 0; i < numq; i++){
        cin >> qtype;
        cin >> qval;
        switch(qtype){
            case(1):
                s.insert(qval);
                break;
            case(2):
                s.erase(qval);
                break;
            case(3):
                iter = s.find(qval);
                if(iter == s.end())
                    cout << "No\n";
                else
                    cout << "Yes\n";
        }
    }   
    return 0;
}



