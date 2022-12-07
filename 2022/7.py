import re
import numpy as np


with open('7.txt') as fh:
    commands = fh.read().split('\n')



def move_out(currentdir):
    lst = currentdir.split(' ')
    return ' '.join(lst[:-1])


folders = {}
files = {}
currentdir = ''
for command in commands:

    if '$ cd' in command:
        if '..' in command:
            currentdir = move_out(currentdir)
        else:
            newdir = re.findall('(?<=\$ cd ).*', command)[0]
            currentdir = currentdir + ' ' + newdir


    elif '$ ls' in command:
        pass


    elif 'dir' in command:
        newdir = re.findall('(?<=dir ).*', command)[0]
        dir = currentdir +' ' + newdir
        if currentdir in folders:
            folders[currentdir].append(dir)
        else:
            folders[currentdir] = [dir]

    else:
        n = int(command.split(' ')[0])
        
        if currentdir in files:
            files[currentdir].append(n)
        else:
            files[currentdir] = [n]



def calculate_size(dir, total_sizes):
    if dir in total_sizes:
        return total_sizes[dir]


    if dir not in folders:
        if dir in files:
            result = sum(files[dir])
        else:
            result = 0

        total_sizes[dir] = result
        return result

    if dir in files:
        result = sum(files[dir])
    else:
        result = 0

    for subdir in folders[dir]:
        result += calculate_size(subdir, total_sizes)

    total_sizes[dir] = result
    return result



total_sizes = {}
calculate_size(' /', total_sizes)


final_result = 0
for x in total_sizes:
    n = total_sizes[x]
    if n <= 100000:
        final_result += n
print(final_result) # part 1: 1454188



### part 2:
used = np.array(list(total_sizes.values()))
required_space = 30000000 - (70000000 - np.max(used))
print(np.min(used[used >= required_space])) # 4183246
