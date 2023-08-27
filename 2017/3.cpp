#include <iostream>
#include <unordered_map>
#include <utility>
// #include <boost/unordered_map.hpp>

using namespace std;


int manhattan_distance(tuple<int, int> coor1, tuple<int, int> coor2) {
    return abs(get<0>(coor1) - get<0>(coor2)) + abs(get<1>(coor1) - get<1>(coor2));
}


int part1(int input) {
    unordered_map<int, tuple<int, int>> map;

    map[1] = make_tuple(0,0);

    int square = 1; // starting point
    int x = 0; int y = 0;  // starting coordinates of square

    int cycle = 2; // cycle height/width (how much we need to move to go around the current map)

    while (square <= input) {
        // go one right
        ++square;
        ++x;
        map[square] = make_tuple(x,y);

        // go up
        for (int i = 0; i < cycle-1; ++i) {
            ++square;
            ++y;
            map[square] = make_tuple(x,y);
        }

        // go left
        for (int i = 0; i < cycle; ++i) {
            ++square;
            --x;
            map[square] = make_tuple(x,y);
        }

        // go down
        for (int i = 0; i < cycle; ++i) {
            ++square;
            --y;
            map[square] = make_tuple(x,y);
        }

        // go right
        for (int i = 0; i < cycle; ++i) {
            ++square;
            ++x;
            map[square] = make_tuple(x,y);
        }

        cycle += 2;
    }

    cout << manhattan_distance(map[1], map[input]) << endl;
    return 0;
}



string make_string(int x, int y) {
    //  tuple is not hashable so use string x,y instead
    return to_string(x) + "," + to_string(y);
}


int get_adjacent_values(int x, int y, unordered_map<string, int> map) {
    // returns sum of neigbors value of coor

    int result = 0;
    for (int i = -1; i < 2; i++) {
        for (int j = -1; j < 2; j++) {
            if (i == 0 && j == 0) {continue;}

            int x_neighbor = x + i;
            int y_neighbor = y + j;

            string key = make_string(x_neighbor, y_neighbor);
            if (map.find(key) != map.end()) { // if key in map
                result += map[key];
            }
        }
    }

    return result;
}


int part2(int input) {
    unordered_map<string, int> map;  // key is coordinates in string, value is the value on that square

    map[make_string(0, 0)] = 1;

    int x = 0; int y = 0;  // starting coordinates of square

    int cycle = 2; // cycle height/width (how much we need to move to go around the current map)

    bool success = false;
    while (true) {
        // go one right
        ++x;
        int value = get_adjacent_values(x, y, map); // calculate value
        map[make_string(x,y)] = value; // store value
        if (value > input) { // check if value larger than input
            cout << value << endl;
            success = true;
        }

        if (success) {break;}

        // go up
        for (int i = 0; i < cycle-1; ++i) {
            ++y;
            int value = get_adjacent_values(x, y, map);
            map[make_string(x,y)] = value;
            if (value > input) {
                cout << value << endl;
                success = true;
                break;
            }
        }

        if (success) {break;}

        // go left
        for (int i = 0; i < cycle; ++i) {
            --x;
            int value = get_adjacent_values(x, y, map);
            map[make_string(x,y)] = value;
            if (value > input) {
                cout << value << endl;
                success = true;
                break;
            }
        }

        if (success) {break;}

        // go down
        for (int i = 0; i < cycle; ++i) {
            --y;
            int value = get_adjacent_values(x, y, map);
            map[make_string(x,y)] = value;
            if (value > input) {
                cout << value << endl;
                success = true;
                break;
            }
        }

        if (success) {break;}

        // go right
        for (int i = 0; i < cycle; ++i) {
            ++x;
            int value = get_adjacent_values(x, y, map);
            map[make_string(x,y)] = value;
            if (value > input) {
                cout << value << endl;
                success = true;
                break;
            }
        }

        if (success) {break;}

        cycle += 2;
    }

    return 0;
}


int main() {
    int input = 361527;  // my input
    part1(input);  // answer part 1: 326
    part2(input);  // answer part 2: 363010
    return 0;
}