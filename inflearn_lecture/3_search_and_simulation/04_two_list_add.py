from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    _ = input()
    list1 = list(map(int, input().split()))
    _ = input()
    list2 = list(map(int, input().split()))
    return list(map(str, sorted(list1 + list2)))

if __name__ == "__main__":
    print(solution(examine=True))