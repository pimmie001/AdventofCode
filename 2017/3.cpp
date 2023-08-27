#include <iostream>
#include <unordered_map>
// #include <boost/unordered_map.hpp>
#include <utility>

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


int main() {
    int input = 361527;  // my input
    part1(input);  // answer part 1: 326

    return 0;
}