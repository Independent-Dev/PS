# binary search example
# 출처: <이것이 취업을 위한 코딩 테스트다>(나동빈, 한빛 미디어) 190page

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 좀 더 보편적으로는 (start + (end - start) // 2)가 맞다고 함
        if array[mid] == target:
            return mid우
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None  # 찾지 못한 경

