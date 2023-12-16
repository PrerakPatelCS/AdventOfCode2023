with open('Appendix.txt', 'r') as file:
    appendix = file.readline().strip().split(',')


def puzzle1() -> None:
    totalHash = 0
    for string in appendix:
        totalHash += hashFunction(string)
    print(totalHash)


def hashFunction(string: str) -> int:
    val = 0
    for c in string:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def puzzle2() -> None:
    boxes = {}
    for string in appendix:
        newString = ''
        getNum = False
        num = 0
        for c in string:
            if c == '=':
                getNum = True
            elif getNum:
                num = int(c)
            elif c == '-':
                continue
            else:
                newString += c
        string = newString
        val = hashFunction(string)
        if val not in boxes:
            boxes[val] = {}

        if num > 0:
            boxes[val][string] = num
        elif string in boxes[val]:
            boxes[val].pop(string)
            if len(boxes[val]) == 0:
                boxes.pop(val)
    totalFocusPower = 0
    for box in boxes:
        slot = 1
        for lens in boxes[box]:
            focusPower = (box + 1) * slot * boxes[box][lens]
            slot += 1
            totalFocusPower += focusPower

    print(totalFocusPower)


puzzle1()
puzzle2()
