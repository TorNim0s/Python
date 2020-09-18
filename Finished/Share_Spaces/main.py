def calculate_ranges(list_core_range):
    list_new_range = []

    for i in list_core_range[0]:
        for x in list_core_range[1]:

            #print(len(list_core_range[0]), len(list_core_range[1]))

            if (i[0] > x[1] or i[1] < x[0]):
                continue

            left_border = (x[0],i[0])[i[0] > x[0]]
            right_border = (x[1],i[1])[i[1] < x[1]]

            for y in list_core_range[2]:
                if (left_border > y[1] or right_border < y[0]):
                    continue

                left_border = (y[0], left_border)[left_border > y[0]]
                right_border = (y[1], right_border)[right_border< y[1]]

                list_new_range.append([left_border,right_border])
    return list_new_range

def main():
    list_core_range =((10, 50), (60, 100), (105, 109), (150, 400), (500, 1000)),\
                     ((20, 40), (50, 90), (100, 200), (300, 450), (750, 810), (900, 980)),\
                     ((30, 70), (80, 250), (300, 500), (700, 850));

    list_new_range = calculate_ranges(list_core_range)
    for num in list_new_range:
        print(num)

if __name__ == "__main__":
    main()