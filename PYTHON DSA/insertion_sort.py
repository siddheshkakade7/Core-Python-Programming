def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1

        elements[j + 1] = anchor


if __name__ == "__main__":
    # elements = [11, 9, 29, 7, 2, 15, 28]
    # insertion_sort(elements)
    # print(elements)
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [7, 3, 2, 15, 11],
        [111, 9, 29, 17, 2, 15, 28],
        [29, 2, 15, 28],
        [9, 29, 72, 2, 15, 28]
    ]
    for elements in tests:
        insertion_sort(elements)
        print("Sorted Array :", elements)
