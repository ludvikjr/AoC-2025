import string


def find_first(line_: string):
    max_ = 0
    max_i = 0
    l = len(line_)

    for i in range(0, l - 1):
        if int(line_[i]) > max_:
            max_ = int(line_[i])
            max_i = i

    return max_, max_i


def find_second(line_: string, first_i: int):
    max_ = 0

    for c in line_[first_i + 1:]:
        if int(c) > max_:
            max_ = int(c)

    return max_


file = open("input", "r")
file_content = file.read()

lines = file_content.split("\n")

sum_ = 0

for line in lines:
    if line.strip() == '':
        continue

    first = find_first(line)
    second = find_second(line, first[1])

    num = int(f'{first[0]}{second}')
    sum_ += num

print(sum_)

file.close()
