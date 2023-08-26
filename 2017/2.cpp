#include <fstream>
#include <iostream>
#include <regex>
#include <string>


int divisible(std::vector<int> numbers) {
    // given a vector of numbers, returns the evenly divisible values (for part 2)

    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i+1; j < numbers.size(); j++) {
            if (numbers[i] % numbers[j] == 0) {
                return numbers[i] / numbers[j];
            } else if (numbers[j] % numbers[i] == 0) {
                return numbers[j] / numbers[i];
            }
        }
    }
    return 0;
}



int main() {
    // ### read input
    std::ifstream inputFile("2.txt");

    std::regex pattern("\\d+");

    std::vector<std::vector<int>> matrix;
    std::string line;  // loop over lines:
    while (std::getline(inputFile, line)) {
        std::sregex_iterator iter(line.begin(), line.end(), pattern);  // find matches
        std::sregex_iterator end = std::sregex_iterator(); // would be the same as: 'std::sregex_iterator end'

        std::vector<int> numbers;  // create vector
        while (iter != end) {
            numbers.push_back(stoi(iter->str()));
            ++iter;
        }
        matrix.push_back(numbers);  // add vector to matrix
    }

    inputFile.close();


    // ### part 1
    int checksum = 0;

    for (int i = 0; i < matrix.size(); ++i) {
        int max = *std::max_element(matrix[i].begin(), matrix[i].end());
        int min = *std::min_element(matrix[i].begin(), matrix[i].end());
        checksum += max - min;
    }

    std::cout << checksum << std::endl;  // answer part 1: 46402


    // ### part 2
    int total = 0;
    for (int i = 0; i < matrix.size(); ++i) {
        total += divisible(matrix[i]);
    }
    std::cout << total; // answer part 2: 265

    return 0;
}