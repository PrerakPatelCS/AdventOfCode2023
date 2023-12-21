import re

with open('Workflow.txt', 'r') as file:
    line = file.readline()
    workflow = {}
    while line and line != "\n":
        items = line.strip()
        items = items[items.find("{") + 1: items.rfind("}")]
        items = items.split(",")

        rules = []

        for item in items:
            match = re.match(r'([a-zA-Z]+)([<>])(\d+):([a-zA-Z]+)', item)
            if match:
                key = match.group(1)
                operator = match.group(2)
                value = int(match.group(3))
                val = match.group(4)

                # Adding the parsed data to the result dictionary
                rules.append((key, operator, value, val))
        rules.append((items[-1]))
        workflow[line[:line.find("{")]] = rules
        line = file.readline()
    ratings = []
    line = file.readline()
    while line:
        line = line.strip()[1: -1].split(",")
        parts = {}
        for item in line:
            part = item[:1]
            num = int(item[2:])
            parts[part] = num
        ratings.append(parts)
        line = file.readline()


def puzzle1() -> int:
    sumRatings = 0
    for parts in ratings:
        register = "in"
        while True:
            for rule in workflow[register]:
                if not type(rule) is tuple:
                    register = rule
                    break
                part, operator, num, newRegis = rule
                if operator == '<':
                    if parts[part] < num:
                        register = newRegis
                        break
                else:
                    if parts[part] > num:
                        register = newRegis
                        break

            if register == 'A':
                for part in parts:
                    sumRatings += parts[part]
                break
            elif register == 'R':
                break

    return sumRatings


print(puzzle1())  # 352052
