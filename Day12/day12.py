import functools

with open('Records.txt', 'r') as file:
    records = []
    for line in file:
        data = line.strip().split()
        data[1] = tuple(map(int, data[1].split(',')))
        records.append(data)


def valid(springs: str, groups: tuple) -> bool:
    separate = []
    group = []
    for c in list(springs):
        if c == '#':
            group.append(c)
        else:
            if len(group) > 0:
                separate.append(group)
                group = []
    if len(group) > 0:
        separate.append(group)
    if len(separate) == len(groups):
        for group1, group2 in zip(separate, groups):
            if len(group1) != group2:
                return False
        return True
    return False

@functools.cache
def backtrack(springs: str, groups: tuple, index: int) -> int:
    if index == len(springs):
        return 1 if valid(springs, groups) else 0
    if springs[index] == '?':
        springsOpt1 = springs[:index] + '.' + springs[index + 1:]
        springsOpt2 = springs[:index] + '#' + springs[index + 1:]
        return backtrack(springsOpt1, groups, index + 1) + backtrack(springsOpt2, groups, index + 1)
    return backtrack(springs, groups, index + 1)

@functools.lru_cache(maxsize=None)
def calc(record: str, groups: tuple) -> int:
    # Base Cases
    if not groups:
        # groups is done and no more # left we are done got a winner
        return 1 if '#' not in record else 0
    if not record:
        # more groups left but no more record, we are done we lost
        return 0

    c = record[0]
    group = groups[0]

    def pound():
        """
        Want to group the first time we see a # with the next
        group size so that we have the groups[0] right
        if everything in there is a # or ? then we fulfill a group
        """
        currGroup = record[:group]
        currGroup = currGroup.replace('?', '#')

        # Check for all # group
        if currGroup != group * '#':
            return 0

        # If the rest of the record is just the last  group, then
        # we are done and only one possibility
        if len(record) == group:
            # make sure this is the last group
            return 1 if len(groups) == 1 else 0

        # Make sure the character that follows this group can be a separator
        # separator is . and can be a separator is ?
        if record[group] in '?.':
            return calc(record[group + 1:], groups[1:])

        # otherwise the group is too big
        return 0

    def period():
        # do nothing move forward
        return calc(record[1:], groups)

    if c == '#':
        ways = pound()
    elif c == '.':
        ways = period()
    elif c == '?':
        ways = period() + pound()
    else:
        raise RuntimeError

    # print(record, groups, ways)
    return ways


def puzzle1() -> None:
    totalNumWays = 0
    for record in records:
        totalNumWays += calc(record[0], record[1])
    print(totalNumWays)


def puzzle2() -> None:
    totalNumWays = 0
    for record in records:
        springs = record[0]
        groups = record[1]
        for i in range(4):
            springs += '?' + record[0]
            groups += record[1]
        # print(springs, groups)
        totalNumWays += calc(springs, groups)
    print(totalNumWays)


puzzle1()  # 7221
puzzle2()  # 7139671893722
