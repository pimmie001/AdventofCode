#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;


void reverse_list(int list[], const int n, const int ind, const int length) {
    // reverses 'list' of length 'n', starting at index 'ind' for 'length' elements

    vector<int> reversed; // part of the list that gets reversed
    for (int i = 0; i < length; i++) {
        reversed.push_back(list[(ind+i)%n]);
    }
    reverse(reversed.begin(), reversed.end()); // reverse the order

    int ind_rev = 0; // index of 'reversed' vector
    for (int i = ind; i < ind + length; i++) {
        list[i%n] = reversed[ind_rev];
        ind_rev++;
    }
}


int main () {
    int lengths[] = {14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244}; // own input
    // int lengths[] = {3,4,1,5}; // example

    // initialise list
    const int n = 256;
    int list[n];
    for (int i = 0; i < n; i++) {
        list[i] = i;
    }

    // loop over lenghts
    int skip_size = 0;
    int current_pos = 0;
    for (int length : lengths) {
        reverse_list(list, n, current_pos, length);
        // for (int i = 0; i < n; i++) {
        //     cout << list[i] << ' ';
        // } cout << endl;
        current_pos += length + skip_size++;
    }
    cout << list[0] * list[1] << endl; // part 1: 1935 

    return 0;
}