def shell_sort(arr):

    size = len(arr)
    gap = size // 2

    while gap > 0:

        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


if __name__ == "__main__":
    # elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [5],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],

    ]
    for elements in tests:
        shell_sort(elements)
        print("Sorted Array:", elements)

