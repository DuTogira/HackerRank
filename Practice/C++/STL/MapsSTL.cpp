//problem: https://www.hackerrank.com/challenges/cpp-maps/problem

#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i, numq, qtype, qval;
    string qname;
    map<string, int> m;  
    map<string, int>::iterator itr;
    cin >> numq;
    for(i = 0; i < numq; i++){
        cin >> qtype;
        cin >> qname;
        itr = m.find(qname);
        switch(qtype){
            case(1):
                cin >> qval;
                if(itr != m.end())
                    m[qname] += qval;
                else
                    m.insert(make_pair(qname, qval));
                break;
            case(2):
                m.erase(qname);
                break;
            case(3):
                if(itr != m.end())
                    cout << itr->second << endl;
                else
                    cout << 0 << endl;
                break;
        }
    }  
    return 0;
}



