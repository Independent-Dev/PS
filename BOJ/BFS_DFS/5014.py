# F: 빌딩의 층 수
# S: 현재 위치
# G: 목표 위치
# U: 위로 몇 칸씩 갈 수 있는지
# D: 아로 몇 칸씩 갈 수 있는지
F, S, G, U, D = list(map(int, input().split()))
visited = [False] * (F + 1)
floors, floors_temp = [S], []
count, is_possible = 0, False

while floors:
    for f in floors:
        if f == G:
            print(count)
            is_possible = True
            break
        f_up, f_down = f + U, f - D
        if f_down > 0 and not visited[f_down]:
            floors_temp.append(f_down)
            visited[f_down] = True
        if f_up <= F and not visited[f_up]:
            floors_temp.append(f_up)
            visited[f_up] = True

    count += 1
    floors, floors_temp = floors_temp[:], []

if not is_possible:
    print("use the stairs")
