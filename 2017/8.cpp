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

    return 0;
}