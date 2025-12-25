
def check_duplicate_combinations(num: int):
    global range_sum
    num_str = str(num)

    l = len(num_str)

    if l % 2 == 1:
        return None

    offset = l//2

    current = num_str[:offset]
    neighbor = num_str[offset:]
    if current == neighbor:
        print(f"Duplicate combination found: {num}, {current}")
        range_sum += num

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
