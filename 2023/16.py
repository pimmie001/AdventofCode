with open('16.txt') as fh:
    grid = fh.read().split('\n')

n = len(grid)
m = len(grid[0])


# own input begins with '\', so starting direction is down (d=1)
beams = [(0,0,1)] # list of beams with (x,y,d) where (x,y) is location and d is direction (0 = right, 1 = down, 2 = left, 3 = up)
energized = set([(0,0)]) # set of energized locations (x,y)
past_beams = set() # set of past beams. Used to determine when to stop loop, also can skip a beam if it is in this set


while beams:
    nr_past_beams = len(past_beams)
    new_beams = []

    for (x,y,d) in beams:
        if (x,y,d) in past_beams: # no need to do the same again (needed for speed)
            continue

        past_beams.add((x,y,d))

        if d == 0 and x < m-1: # right
            x += 1
            energized.add((x,y))

            if grid[y][x] == '\\':
                new_beams.append((x,y,1))
            elif grid[y][x] == '/':
                new_beams.append((x,y,3))
            elif grid[y][x] == '|':
                new_beams.append((x,y,1))
                new_beams.append((x,y,3))
            else:
                new_beams.append((x,y,d))

        elif d == 1 and y < n-1: # down
            y += 1
            energized.add((x,y))

            if grid[y][x] == '\\':
                new_beams.append((x,y,0))
            elif grid[y][x] == '/':
                new_beams.append((x,y,2))
            elif grid[y][x] == '-':
                new_beams.append((x,y,0))
                new_beams.append((x,y,2))
            else:
                new_beams.append((x,y,d))

        elif d == 2 and x > 0: # left
            x -= 1
            energized.add((x,y))

            if grid[y][x] == '\\':
                new_beams.append((x,y,3))
            elif grid[y][x] == '/':
                new_beams.append((x,y,1))
            elif grid[y][x] == '|':
                new_beams.append((x,y,1))
                new_beams.append((x,y,3))
            else:
                new_beams.append((x,y,d))

        elif d == 3 and y > 0: # up
            y -= 1
            energized.add((x,y))

            if grid[y][x] == '\\':
                new_beams.append((x,y,2))
            elif grid[y][x] == '/':
                new_beams.append((x,y,0))
            elif grid[y][x] == '-':
                new_beams.append((x,y,0))
                new_beams.append((x,y,2))
            else:
                new_beams.append((x,y,d))

    beams = new_beams

    if nr_past_beams == len(past_beams):
        break


print(f'Answer part 1: {len(energized)}') # part 1: 7860
