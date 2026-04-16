people,matches = map(int, input().split())

match = [list(map(int, input().split())) for i in range(matches)]

result = [["-"] * people for _ in range(people)]

for a, b in match:
    a -=1
    b -=1
    result[a][b] = "o"
    result[b][a] = "x"

for row in result:
    print(" ".join(row))  