#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;


// own struct and function for finding max value and index in array
struct MaxResult {
    int value;
    int index;
};

MaxResult find_max(int state[], int n) {
    MaxResult result;
    result.value = state[0];
    result.index = 0;

    for (int i = 1; i < n; i++) {
        if (state[i] > result.value){
            result.value = state[i];
            result.index = i;
        }
    }
    return result;
}


// hash for state array
size_t hash_state(const int state[], size_t n) {
    size_t hash_value = 0;
    for (size_t i = 0; i < n; ++i) {
        hash_value = hash_value * 31 + state[i];
    }
    return hash_value;
}


// reallocation
int change_state(int state[], int n) {
    MaxResult max_result = find_max(state, n);

    int new_value_i = 0;
    int i = (max_result.index + 1) % n;

    for (int _ = 0; _ < max_result.value; _++) {
        if (i != max_result.index) {
            state[i]++;
        }
        else {
            new_value_i++;
        }
        i = (i+1) % n;
    }

    state[max_result.index] = new_value_i;

    return 0;
}


// check if state already in previous states
int check_state(int state[], int n, int iteration, unordered_map<size_t, int>& previous_states) {
    size_t key = hash_state(state, n);

    if (previous_states.find(key) != previous_states.end()) {
        return previous_states[key];
    }
    previous_states[key] = iteration; // add value in-place
    return 0;
}


int main() {
    // int state[] = {0, 2, 7, 0}; // example
    int state[] = {14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4}; // own input
    int n = sizeof(state) / sizeof(state[0]);

    unordered_map<size_t, int> previous_states;
    int iteration = 0;
    int success = check_state(state, n, iteration, previous_states); // add state to map

    while (true) {
        change_state(state, n);
        iteration++;
        success = check_state(state, n, iteration, previous_states);
        if (success) {
            cout << iteration << endl; // part 1: 11137
            cout << iteration - success << endl; // part 2: 1037
            break;
        }
    }

    return 0;
}