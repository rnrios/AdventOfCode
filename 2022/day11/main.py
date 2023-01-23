import re


def prod_list(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * prod_list(arr[1:])


class Monkey:
    def __init__(self, items, ops, test, decision):
        self.items = items
        self.ops = ops
        self.test = test
        self.decision = decision
        self.worry = 0
        self.inspections = 0

    def operate(self, item, num, den):
        if self.ops[0] == '+':
            worry = (item + num) // den
        else:
            worry = (item * num) // den
        return worry

    def play_round(self, list_of_monkeys, hash_num, thresh=True):
        den = 3 if thresh else 1
        for item in self.items:
            num = item if self.ops[2:] == 'old' else int(self.ops[2:])
            self.worry = self.operate(item, num, den)
            destination = self.decision[self.worry % self.test == 0]
            if thresh:
                list_of_monkeys[destination].items.append(self.worry)
            else:
                list_of_monkeys[destination].items.append(self.worry % hash_num)
            self.items = self.items[1:]
            self.inspections += 1


def get_monkeys():
    monkeys = []
    t0 = t1 = op = div = items_list = None
    for i, line in enumerate(open('input.txt').readlines()):
        if re.findall(r'items', line):
            items_list = [int(item) for item in re.findall(r'\d+', line)]
        if re.findall(r'Operation', line):
            op = line.split('old ')[1][:-1]
        if re.findall(r'Test', line):
            div = int(re.findall(r'\d+', line)[0])
        if re.findall(r'true', line):
            t1 = int(re.findall(r'\d+', line)[0])
        if re.findall(r'false', line):
            t0 = int(re.findall(r'\d+', line)[0])
        if line == '\n' or line[-1] != '\n':
            to_throw = [t0, t1]
            monkey = Monkey(items_list, op, div, to_throw)
            monkeys.append(monkey)
    return monkeys


def play(monkeys, rounds, w_factor=True):
    hash_num = prod_list([m.test for m in monkeys])
    for i in range(rounds):
        for monkey in monkeys:
            monkey.play_round(monkeys, hash_num, w_factor)
    return monkeys


monkeys_list = play(get_monkeys(), 20)
print(f'Part 1: {prod_list(sorted([m.inspections for m in monkeys_list])[-2:])}')
monkeys_list = play(get_monkeys(), 10000, False)
print(f'Part 2: {prod_list(sorted([m.inspections for m in monkeys_list])[-2:])}')
