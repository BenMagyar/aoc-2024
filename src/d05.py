from collections import defaultdict
from functools import cmp_to_key

def prepare(input):
    split_on = next(i for i, v in enumerate(input) if v == '')
    rules, updates = input[:split_on], input[split_on + 1:]
    
    rule_matches = defaultdict(lambda: {})
    for before, value in [rule.split('|') for rule in rules]:
        rule_matches[before][value] = True

    updates = list(list(update.split(',')) for update in updates)

    return (rule_matches, updates)

def is_valid(rules, update):
    if len(update) == 1:
        return True
    
    for value in update[1:]:
        if value not in rules[update[0]]:
            return False

    return is_valid(rules, update[1:])
    
def part_one(input):
    rules, updates = input
    return sum(int(update[len(update) // 2]) for update in updates if is_valid(rules, update))

def part_two(input):
    rules, updates = input
    invalid = [update for update in updates if not is_valid(rules, update)]

    memory = defaultdict()
    def compare(a, b):
        after = list(rules[a].keys())
        checked = []
        while len(after) > 0:
            current = after.pop()
            if current == b:
                return -1
            checked.append(current)
            after.extend(key for key in rules[current].keys() if key not in checked)
        return 1
    
    sort_key = cmp_to_key(compare)
    invalid = [sorted(update, key=sort_key) for update in invalid]
    
    return sum(int(update[len(update) // 2]) for update in invalid)
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 143
    assert part_two(input) == 123

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
