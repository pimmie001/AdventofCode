#include <fstream>
#include <iostream>
#include <string>


std::string read_file() {
    std::ifstream inputFile("1.txt");

    std::string input;  // Declare the 'input' variable

    if (inputFile.is_open()) {
        std::getline(inputFile, input);  // Read a line and store in 'input' variable
        inputFile.close();  // Close the file
    }

    // std::cout << input << std::endl; // print input
    return input;
}


int captcha(std::string input) {
    int result = 0;

    for (size_t i = 0; i < input.length(); ++i) {
        char digit = input[i];
        char next_digit = input[(i + 1) % input.length()];

        if (digit == next_digit) {
            result += digit - '0';
        }
    }

    return result;
}


int main() {
    std::string input = read_file();  // read the input
    int result = captcha(input);  // do the captcha

    std::cout << result << std::endl;  // answer part 1: 997
    return 0;
}