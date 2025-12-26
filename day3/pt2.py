import string


def find_next(line_: string, prev_ind: int, remaining_cnt: int):
    max_ = 0
    max_i = 0
    l = len(line_)

    for i in range(prev_ind + 1, l - remaining_cnt + 1):
        if int(line_[i]) > max_:
            max_ = int(line_[i])
            max_i = i

    return max_, max_i


file = open("input", "r")
file_content = file.read()

lines = file_content.split("\n")

sum_ = 0

for line in lines:

    if line.strip() == '':
        continue

    prev_index = -1
    num_str = ""

    for j in range(0, 12):
        res = find_next(line, prev_index, 12 - j)
        prev_index = res[1]
        num_str += str(res[0])

    num = int(num_str)
    sum_ += num

print(sum_)

file.close()
