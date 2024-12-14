input = "125 17" # example
input = "6563348 67 395 0 6 4425 89567 739318" # own input

stones = [int(x) for x in input.split()]


def apple_rule(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        return [int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])]

    return [stone*2024]


for _ in range(25):
    new_stones = []
    for stone in stones:
        new_stones.extend(apple_rule(stone))
    stones = new_stones
print(len(stones))
