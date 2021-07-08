from examine.examine import examine

@examine
def solution(*args):
    pass

if __name__ == "__main__":
    N = int(input())
    target = [input().strip().lower() for _ in range(N)]
    for i, t in enumerate(target, start=1):
        print(f"#{i} {'YES' if t == t[::-1] else 'NO'}")
