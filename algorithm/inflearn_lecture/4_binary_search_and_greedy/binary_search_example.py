def binary_search(start, target, arr):
    stop = len(arr)
    while start <= stop:
        middle = (start + stop) // 2
        if arr[middle] == target:
            return middle
        if arr[middle] > target:
            stop = middle - 1
        else:
            start = middle + 1

    else:
        return "not possible"

