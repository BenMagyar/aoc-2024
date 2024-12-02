from math import copysign

def prepare(input):
    return [list(map(int, line.split(' '))) for line in input]

def is_ok(line, corrections = 0):
    subs = list(map(lambda p: p[1] - p[0], list(zip(line, line[1:]))))
    sign = copysign(1, subs[0])

    bad_idx = next((i for i, sub in enumerate(subs) if sign != copysign(1, sub)), None)
    bad_idx = bad_idx or next((i for i, sub in enumerate(subs) if (abs(sub) not in range(1, 4))), None)
    
    if bad_idx is not None and corrections > 0:
        paths = [
            line[:bad_idx - 1] + line[bad_idx:],
            line[:bad_idx] + line[bad_idx + 1:],
            line[:bad_idx + 1] + line[bad_idx + 2:],
        ]
        return any(is_ok(path, corrections - 1) for path in paths)

    return bad_idx is None

def part_one(input, on_failure = None):
    return len([line for line in input if is_ok(line)])

def part_two(input):
    return len([line for line in input if is_ok(line, 1)])
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 2
    assert part_two(input) == 4

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
