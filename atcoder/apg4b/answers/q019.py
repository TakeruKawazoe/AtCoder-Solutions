def f0(N):
    return 1

def f1(N, M):
    s = 0
    for i in range(N):
        s += 1
    for i in range(M):
        s += 1
    return s

def f2(N):
    s = 0
    for i in range(N):
        t = N
        cnt = 0
        while t > 0:
            cnt += 1
            t //= 2
        s += cnt
    return s

def f3(N):
    s = 0
    for i in range(3):
        for j in range(3):
            s += 1
    return s

def f4(N):
    s = 0
    for i in range(N):
        for j in range(N):
            s += i + j
    return s

def f5(N, M):
    s = 0
    for i in range(N):
        for j in range(M):
            s += i + j
    return s

# 標準入力から値を取得
N, M = map(int, input().split())

# 計算結果の変数を初期化
a0, a1, a2, a3, a4, a5 = -1, -1, -1, -1, -1, -1

# 計算量が最も大きいものを 1 つだけコメントアウトする (先頭に # をつける)
a0 = f0(N)
a1 = f1(N, M)
a2 = f2(N)
a3 = f3(N)
# a4 = f4(N)
a5 = f5(N, M)

# 結果を出力
print(f"f0: {a0}")
print(f"f1: {a1}")
print(f"f2: {a2}")
print(f"f3: {a3}")
print(f"f4: {a4}")
print(f"f5: {a5}")
