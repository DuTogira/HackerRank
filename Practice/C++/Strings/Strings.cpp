//problem: https://www.hackerrank.com/challenges/c-tutorial-strings/problem

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b, combined;
    cin >> a;
    cin >> b;
    combined = a + b;
    cout << a.size() << " " << b.size() << endl;
    cout << combined << endl;
    swap(a[0], b[0]);
    cout << a << " " << b << endl;
    return 0;
}
