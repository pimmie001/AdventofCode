#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>

using namespace std;


int calculate_values(const string word, map <string, string> & neighbor_above, 
                    map <string, int> weight, map <string, int> & values) {
    // calculates the weight the word is supporting (not its own weight)


    // no other words above:
    if (neighbor_above[word] == "") {
        values[word] = weight[word];
        return weight[word];
    }

    // see if already calculated
    if (values.find(word) != values.end()) {
        return values[word];
    }

    // calculate total value
    int result = weight[word];
    string substring = neighbor_above[word];
    size_t i = 0;
    size_t start = 0;
    while (i < substring.size()) {
        if (substring[i] == ',') {
            string word2 = substring.substr(start, i-start);
            result += calculate_values(word2, neighbor_above, weight, values);
            i += 2;
            start = i;
        }
        else {
            i++;
        }
    }

    values[word] = result; // add to values
    return result;
}


bool vector_equal(vector <int> vec) {
    if (vec.empty()) {
        return true;
    }

    int first = vec[0];
    for (int i = 1; i < vec.size(); i++) {
        if (vec[i] != first) {
            return false;
        }
    }

    return true;
}


int check_values(const string word, map <string, string> & neighbor_above, map <string, int> & values) {
    // checks all values starting at word and returns the numbers if they are different


    // no other words above:
    if (neighbor_above[word] == "") { 
        return 0;
    }

    // find values of above neighbors
    string substring = neighbor_above[word];
    size_t i = 0;
    size_t start = 0;
    vector <int> weights_neighbors;
    vector <string> neighbors;
    while (i < substring.size()) {
        if (substring[i] == ',') {
            string word2 = substring.substr(start, i-start);
            weights_neighbors.push_back(values[word2]);
            neighbors.push_back(word2);
            check_values(word2, neighbor_above, values); // check recursive
            i += 2;
            start = i;
        }
        else {
            i++;
        }
    }

    // check values
    bool correct = vector_equal(weights_neighbors);
    if (!correct) {
        // for (int i = 0; i < weights_neighbors.size(); i++) {
        //     cout << weights_neighbors[i] << " " << neighbors[i] << " ";
        // }
        // cout << endl;
    }
    return 0; 
}


int main() {
    ifstream inputFile("7.txt");

    map <string, string> neighbor_below;
    map <string, string> neighbor_above;
    map <string, int> weight;

    string line;
    while (getline(inputFile, line)) {
        // find first word
        size_t space = line.find(' ');
        string word = line.substr(0, space);

        // find weight
        size_t open = line.find("(");
        size_t close = line.find(")");
        weight[word] = stoi(line.substr(open+1, close-open-1));

        // set value if it doesnt already have one
        if (neighbor_below.find(word) == neighbor_below.end()) {
            neighbor_below[word] = "";
        }

        // find neighbors
        size_t arrow = line.find("->");
        if (arrow != string::npos) {
            string subline = line.substr(arrow+3) + ",";
            neighbor_above[word] = subline; // set above neigbors
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
        else {
            neighbor_above[word] = "";
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


    // calculate all values
    map <string, int> values; // the sum of the weigts of the words above
    calculate_values(word, neighbor_above, weight, values); // calculates all values
    check_values(word, neighbor_above, values);

    // last part hardcoded
    // 2615 vmttcwe 2607 ukwlfcf 2607 zzpevgd 
    cout << weight["vmttcwe"] - (2615 - 2607) << endl; // part 2: 2310

    return 0;
}