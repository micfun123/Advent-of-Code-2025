dial_cur = 50
dial_max = 99
mod = dial_max + 1
hit_zero = 0

with open("1.in") as f:
    instruct = f.read().split()

for i in instruct:
    direction = i[0]
    amount = int(i[1:])

    if direction == "L":
        dial_cur = (dial_cur - amount) % mod
    else:
        dial_cur = (dial_cur + amount) % mod

    if dial_cur == 0:
        hit_zero += 1

print(dial_cur)
print(hit_zero)


# PART 2

with open("1.in") as f:
    instruct = f.read().split()

dial_cur = 50
dial_max = 99
mod = dial_max + 1
hit_zero = 0

for instruction in instruct:
    direction = instruction[0]
    amount = int(instruction[1:])

    if direction == "R":
        raw_position = dial_cur + amount
        loops = raw_position // mod
    else:
        raw_position = dial_cur - amount
        # count multiples of mod in the decreasing range (s-1 .. s-a)
        loops = ((dial_cur - 1) // mod) - ((raw_position - 1) // mod)

    hit_zero += loops
    dial_cur = raw_position % mod

print(dial_cur)
print(hit_zero)
