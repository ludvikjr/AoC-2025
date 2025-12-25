
def check_duplicate_combinations(num: int):
    global range_sum
    num_str = str(num)

    l = len(num_str)

    if l == 1:
        return None

    offset = 1

    while offset <= l//2 + l % 2:
        combination = num_str[:offset]
        chunks = [num_str[i:i+offset] for i in range(offset, l, offset)]
        duplicate = True
        for chunk in chunks:
            if combination != chunk:
                duplicate = False
                break

        if duplicate:
            print(f"Duplicate combination found: {num}, {combination}")
            range_sum += num
            break

        offset += 1

    return None


file = open("input", "r")
file_content = file.read()

ranges_str = file_content.split(",")
ranges = [range(int(a), int(b)+1) for a,b in (r.split('-') for r in ranges_str)]

range_sum = 0

for r in ranges:
    for number in r:
        check_duplicate_combinations(number)

print(range_sum)

file.close()
