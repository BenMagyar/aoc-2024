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
    
    sort_key = cmp_to_key(lambda a, b: -1 if b in rules[a].keys() else 1)
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
