def swap(a, b, arr):
    if a != b:
        # arr[a], arr[b] = arr[b], arr[a]
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    # start = pivot_index + 1
    # end = len(elements) - 1
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    return end


def quick_sort(elements, start, end):
    # partition(elements, start, end)
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)  # left partition
        quick_sort(elements, pi + 1, end)  # right partition


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [29, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # quick_sort(elements, 0, len(elements) - 1)
    # print(elements)

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print("Sorted Array :", elements)
