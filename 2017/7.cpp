#include <iostream>
#include <string>
#include <fstream>
#include <map>

using namespace std;


int main() {
    ifstream inputFile("7.txt");

    map <string, string> neighbor_below;

    string line;
    while (getline(inputFile, line)) {
        // find first word
        size_t space = line.find(' ');
        string word = line.substr(0, space);

        // set key if it doesnt already have one
        if (neighbor_below.find(word) == neighbor_below.end()) {
            neighbor_below[word] = "";
        }

        // find neighbors
        size_t arrow = line.find("->");
        if (arrow != string::npos) {
            string subline = line.substr(arrow+3) + ",";
            size_t start = 0;
            size_t i = 0;
            while (i < subline.size()) {
                if (subline[i] == ',') {
                    string word2 = subline.substr(start, i-start);
                    neighbor_below[word2] = word; // set below neigbor
                    i += 2;
                    start = i;
                }
                else {
                    i++;
                }
            }
        }
    }

    string word = "fjkfpm"; // begin with a random word (must be in the tower somewhere)
    while (true) {
        if (neighbor_below[word] == "") {
            break;
        }
        word = neighbor_below[word];
    }
    cout << word << endl; // part 1: cqmvs


    return 0;
}