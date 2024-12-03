import re
from functools import reduce

def prepare(input):
    return input
    
def part_one(input):
    matches = [re.findall(r'mul\((\d+),(\d+)\)', line) for line in input]
    return sum(int(x) * int(y) for line in matches for x, y in line)

def part_two(input):
    matches = [re.findall(r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))', line) for line in input]
    
    enabled, sum = True, 0
    for line in matches:
        for x, y, dont, do in line:
            if do != '':
                enabled = True
            elif dont != '':
                enabled = False
            elif enabled:
                sum += (int(x) * int(y))
    
    return sum
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 161
    assert part_two(input) == 48

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
    