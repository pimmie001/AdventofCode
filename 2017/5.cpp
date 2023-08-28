#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

using namespace std;


int print_vector(vector<int> v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << ' ';
    }
    cout << endl;
    return 0;
}


int part1(vector<int> instructions) {
    int turns = 0;
    int ind = 0;
    while (ind < instructions.size()) {
        int jump = instructions[ind];
        ++instructions[ind];
        ind += jump;
        turns += 1;
    }
    cout << turns << endl;  // part 1: 375042

    return 0;
}



int main () {
    ifstream inputFile("5.txt");

    vector<int> instructions;
    int num;
    while (inputFile >> num) {
        instructions.push_back(num);
    }

    part1(instructions); // part 1: 375042

    return 0;
}