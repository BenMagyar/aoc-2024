def prepare(input):
    return (
        sorted([int(line.split('   ')[0]) for line in input]),
        sorted([int(line.split('   ')[1]) for line in input]),
    )
    
def part_one(input):
    return sum(abs(input[0][i] - input[1][i]) for i in range(len(input[0])))

def part_two(input):
    return sum(v * input[1].count(v) for v in input[0])
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 11
    assert part_two(input) == 31

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
