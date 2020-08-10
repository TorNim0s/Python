def parse_ranges(ranges_string):
    gen = (n for n in ranges_string.split(","))
    gen2 = (n.split("-") for n in gen)
    gen3 = []
    for start, stop in gen2:
        for num in range(int(start), int(stop) + 1):
            gen3.append(num)

    return gen3

print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))

