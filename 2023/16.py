with open('16.txt') as fh:
    grid = fh.read().split('\n')

n = len(grid)
m = len(grid[0])


def get_nr_energized(start_beam):
    """Start beam should be outside of grid, because first occuring space can be a mirror or splitter"""

    beams = [start_beam] # list of beams with (x,y,d) where (x,y) is location and d is direction (0 = right, 1 = down, 2 = left, 3 = up)
    energized = set([(0,0)]) # set of energized locations (x,y)
    past_beams = set() # set of past beams --> can skip a beam if it is in this set

    while beams:
        new_beams = []

        for (x,y,d) in beams:
            if (x,y,d) in past_beams: # no need to do the same again
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

    return len(energized) 


### part 1
print(get_nr_energized((-1,0,0))) # start from (-1,0) with direction 1 = right so first move will be to (0,0)
# part 1: 7860

### part 2
maximum = 0
for x in range(m):
    maximum = max(maximum, get_nr_energized((x,-1,1))) # from above
    maximum = max(maximum, get_nr_energized((x,n,3))) # from below
for y in range(n):
    maximum = max(maximum, get_nr_energized((-1,y,0))) # from the left
    maximum = max(maximum, get_nr_energized((m,y,2))) # from the right
print(maximum) # part 2: 8331 