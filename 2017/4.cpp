#include <iostream>
#include <set>
#include <vector>
#include <fstream>
#include <string>
#include <regex>


using namespace std;


bool valid(vector<string> vect) {
    set<string> my_set;
    for (const string& x : vect) {
        if (my_set.find(x) != my_set.end()) {
            return false;
        }
        my_set.insert(x);
    }
    return true;
}


int main () {
    ifstream inputFile("4.txt");
    regex pattern("[a-zA-Z]+");

    int result = 0;
    string line;
    while (getline(inputFile, line)) {
        sregex_iterator iter(line.begin(), line.end(), pattern); // find matches
        sregex_iterator end = sregex_iterator();

        vector<string> vect;
        while (iter != end) {
            vect.push_back(iter->str());
            ++iter;
        }

        result += valid(vect);
    }

    cout << result << endl; // part 1: 451

    return 0;
}