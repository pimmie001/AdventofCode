with open('12.txt') as fh:
    content = fh.read().split('\n')

records = []
conditions = []
for line in content:
    rec, con = line.split(' ')
    records.append(rec)
    conditions.append([int(x) for x in con.split(',')])

## unfold 
for i in range(len(records)):
    records[i] += ('?' + records[i])*4
    conditions[i] *= 5



def get_score(record, condition, prev=0, memo={}):
    """Function will exhaustively explore all options but will stop as soon as it is clear that current string (record) 
    is not possible. Remembers combinations of (record, prev, condition) in memo (otherwise would take very long)"""

    ## check if in memo
    if (record, prev, condition) in memo:
        return memo[(record, prev, condition)]
    original_condition = condition # since 'condition' changes in function


    ## find numbers till a ? appears
    i = 0
    count = prev
    while i < len(record):
        if record[i] == '?':
            # return sum of . or # (and store in memo)
            result = get_score('.' + record[i+1:], condition, prev=count, memo=memo) + get_score('#' + record[i+1:], condition, prev=count, memo=memo)
            memo[(record, prev, original_condition)] = result
            return result

        if record[i] == '#':
            count += 1

        elif count > 0:
            if condition and condition[0] == count: # remove last condition as it has been satisfied
                condition = condition[1:]
                count = 0
            else: # contradiction --> cannot be feasible
                return 0

        i += 1


    if count > 0:
        if condition and condition[0] == count:
            condition = condition[1:]
        else:
            return 0

    if condition:
        return 0
    return 1



total = 0
for i in range(len(conditions)):
    total += get_score(records[i], tuple(conditions[i]))
print(total) # part 2: 17391848518844
