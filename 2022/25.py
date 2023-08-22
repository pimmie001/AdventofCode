with open ('25.txt') as fh:
    numbers = fh.read().split('\n')


### 1. get the sum in decimal
def SNAFU_to_dec(number):
    result = 0
    for i in range(len(number)):
        if number[i] == '=':
            n = -2
        elif number[i] == '-':
            n = -1
        else:
            n = int(number[i])
        result += n * 5 ** (len(number) - i - 1)
    return result


total_dec = 0
for n in numbers:
    total_dec += SNAFU_to_dec(n)


### 2. convert to SNAFU
def lowest_power5(number):
    # returns the smallest value of i such that 5**i > number
    if number == 0:
        return 0

    i = 0
    while True:
        if number < 5 ** i:
            return i - 1 
        i += 1


def get_powers_of_5(number):
    result = [0]
    x = lowest_power5(number)

    while x >= 0:
        div, number = divmod(number, 5**x)
        result.append(div)
        x -= 1

    return result


def dec_to_SNAFU(number):
    powers = get_powers_of_5(number)

    result = ''
    recall = 0 # number to recall when adding numbers: (4 = 5 - 1) so we 'recall' 1 when we move to the next power
    for n in powers[::-1]:
        n = n + recall
        if n <= 2:
            result += str(n)
            recall = 0
        elif n == 3: # 5 minus 2
            result += '='
            recall = 1
        elif n == 4: # 5 minus 1
            result += '-'
            recall = 1
        elif n == 5:
            result += '0'
            recall = 1

    result = result[::-1]
    result = result.lstrip('0') # remove leading zeros
    return result


### answer day 25
print(dec_to_SNAFU(total_dec)) # 2-2=21=0021=-02-1=-0 

