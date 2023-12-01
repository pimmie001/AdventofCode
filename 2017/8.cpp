#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <vector>

using namespace std;


int get_value(const string key, map<string, int> & values) {
    if (values.find(key) == values.end()) {
        return 0;
    }
    return values[key];
}


int main() {
    ifstream file("8.txt");

    map<string, int> values;
    int all_time_max = 0;

    string line;
    while (getline(file, line)) {
        // get all words
        istringstream iss(line);
        vector<string> words;

        string word;
        while (iss >> word) {
            words.push_back(word);
        }

        // check if statement
        bool success = false;
        if (words[5] == ">") {
            success = get_value(words[4], values) > stoi(words[6]);
        } else if (words[5] == ">=") {
            success = get_value(words[4], values) >= stoi(words[6]);
        } else if (words[5] == "<") {
            success = get_value(words[4], values) < stoi(words[6]);
        } else if (words[5] == "<=") {
            success = get_value(words[4], values) <= stoi(words[6]);
        } else if (words[5] == "==") {
            success = get_value(words[4], values) == stoi(words[6]);
        } else if (words[5] == "!=") {
            success = get_value(words[4], values) != stoi(words[6]);
        } else {cout << words[5] << endl;}


        // execute
        if (success) {
            if (words[1] == "inc") {
                values[words[0]] = get_value(words[0], values) + stoi(words[2]);
                if (values[words[0]] > all_time_max) { // for part 2
                    all_time_max = values[words[0]];
                }
            }
            else {
                values[words[0]] = get_value(words[0], values) - stoi(words[2]);
            }
            
        }
    }

    // find maximum value
    int maximum = -9999;
    for (const auto& pair : values) {
        const int& val = pair.second;
        if (val > maximum) {
            maximum = val;
        }
    }
    cout << maximum << endl; // part 1: 4066
    cout << all_time_max << endl; //part 2: 4829

    return 0;
}