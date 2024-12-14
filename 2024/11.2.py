from collections import Counter

input = "125 17" # example
input = "6563348 67 395 0 6 4425 89567 739318" # own input

stones = [int(x) for x in input.split()]


def apple_rule(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        return [int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])]

    return [stone*2024]


def find_number_stones(stones, iterations):
    """
    Finds the number of stones after applying the number of iterations
    stones should be a dictinary with keys stone numbers and values the count of stones ({1:2, 3:4} would mean [1,1,3,3,3,3]
    iterations is the number of iterations left
    """

    if iterations == 0: # base case
        return sum(stones.values())

    new_stones = {}
    for stone, count in stones.items():
        for new_stone in apple_rule(stone):
            if new_stone in new_stones:
                new_stones[new_stone] += count
            else:
                new_stones[new_stone] = count

    return find_number_stones(new_stones, iterations-1)


result = find_number_stones(Counter(stones), 75)
print(result) # part 2: 220357186726677
