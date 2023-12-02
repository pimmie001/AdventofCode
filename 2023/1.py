with open('1.txt') as fh:
    content = fh.read().split('\n')

total = 0
for line in content:
    found_first = False
    last = None
    for letter in line:
        if letter.isnumeric():
            if found_first:
                last = letter
            else:
                first = letter
                found_first = True

    if last:
        total += int(first+last)
    else:
        total += int(first+first)

print(total) # part 1: 55447



number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def extract_numbers(string):
    result = []

    for i in range(len(string)):
        if string[i].isnumeric():
            result.append(string[i])
            continue

        for word in number_dict:
            if string[i:i+len(word)] == word:
                result.append(number_dict[word])
                continue

    return result


total2 = 0
for line in content:
    numbers = extract_numbers(line)
    if len(numbers) == 1:
        numbers *= 2

    total2 += int(numbers[0] + numbers[-1])

print(total2) # part 2: 54706
