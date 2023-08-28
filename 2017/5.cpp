#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

using namespace std;


int part1(vector<int> instructions) {
    int turns = 0;
    int ind = 0;
    while (ind < instructions.size()) {
        int jump = instructions[ind];
        ++instructions[ind];
        ind += jump;
        turns += 1;
    }
    cout << turns << endl;

    return 0;
}


int part2(vector<int> instructions) {
    int turns = 0;
    int ind = 0;
    while (ind < instructions.size()) {
        int jump = instructions[ind];
        if (jump >= 3) {
            --instructions[ind];
        }
        else {
            ++instructions[ind];
        }
        ind += jump;
        turns += 1;
    }
    cout << turns << endl;

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
    part2(instructions); // part 2: 28707598

    return 0;
}