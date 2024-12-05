from itertools import product

xmas = 'XMAS'

def prepare(input):
    return [list(line) for line in input]

def part_one(input):
    height, width = len(input), len(input[0])
    get = lambda x, y: input[y][x] if y >= 0 and y < height and x >= 0 and x < width else None
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def search(x, y, dx, dy, current = 'X'):
        if get(x, y) == current:
            if current == 'S':
                return 1
            return search(x + dx, y + dy, dx, dy, xmas[xmas.index(current) + 1])
        return 0

    matches = 0
    for y in range(height):
        for x in range(width):
            matches += sum((search(x, y, dx, dy) for dx, dy, in directions))

    return matches

def part_two(input):
    height, width = len(input), len(input[0])
    get = lambda x, y: input[y][x] if y >= 0 and y < height and x >= 0 and x < width else None
    masks = [list('MS'), list('SM')]

    def search(x, y):
        if get(x, y) != 'A':
            return 0
        
        if [get(x - 1, y - 1), get(x + 1, y + 1)] in masks:
            if [get(x - 1, y + 1), get(x + 1, y - 1)] in masks:
                return 1

        return 0

    matches = 0    
    for y in range(height):
        for x in range(width):
            matches += search(x, y)
    
    return matches
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 18
    assert part_two(input) == 9

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))

