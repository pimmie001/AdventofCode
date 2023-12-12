### read data

with open('12.txt') as fh:
    content = fh.read().split('\n')

records = []
conditions = []
for line in content:
    rec, con = line.split(' ')
    records.append(rec)
    conditions.append([int(x) for x in con.split(',')])


### functions

def get_condition(record):
    # given a record without ?, get the condition

    count = 0
    condition = []
    for x in record:
        if x == '#':
            count += 1
        else:
            if count:
                condition.append(count)
            count = 0
    if count:
        condition.append(count)
    return condition


def match_condition(record, condition):
    return get_condition(record) == condition


def extend_records(all_records, i):
    # at index i, replace all records with # and .
    new_records = []
    for record in all_records:
        new_records.append(record[:i] + '#' + record[i+1:])
        new_records.append(record[:i] + '.' + record[i+1:])
    return new_records


def get_all_records(record):
    # given a record, returns a list of records containing all options

    all_records = [record]
    while '?' in all_records[-1]:
        i = all_records[-1].index('?')
        all_records = extend_records(all_records, i)
    return all_records


### get total
total = 0
for i in range(len(records)):
    for record in get_all_records(records[i]):
        total += match_condition(record, conditions[i])
print(total) # part 1: 7047
