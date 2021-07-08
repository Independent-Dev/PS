from examine.examine import examine
import sys

@examine
def solution(**kwargs):
    if kwargs['examine']:
        sys.stdin = open(f"{kwargs['folder_path']}/in{kwargs['id']}.txt", 'r')
    # 1.가장 무식한 방법 start, stop = max(video_lengths), sum(video_length)으로 두고 이걸 줄여나가는 것
    N, M = map(int, input().split())
    video_lengths = list(map(int, input().split()))
    start, stop = max(video_lengths), sum(video_lengths)  # 여기에서 stop을 뭘로 잡아야 하나...
    result = stop
    while start <= stop:
        mid = (start + stop) // 2
        temp, count = mid, 1
        for length in video_lengths:
            if (temp - length) >= 0:
                temp -= length
            else:
                count += 1
                if count > M:
                    start = mid + 1
                    break
                temp = mid - length
        else:
            result = min(result, mid)
            stop = mid - 1
    return [str(result)]

if __name__ == "__main__":
    print(solution(examine=True))
