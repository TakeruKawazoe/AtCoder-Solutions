data = [int(c) for c in input().split()]
# dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
ans = False # 始めはfalseにしておき、条件を満たすときにtrueになるようにする
for k in range(len(data)-1):
    if data[k]==data[k+1]:
        ans = True
if ans:
    print("YES")
else:
    print("NO")