Number,Total_match = map(int,input().split())

just = 0

Apple = list(map(int,input().split()))
Pineapple = list(map(int,input().split()))


for i in range(Number):
  for j in range(Number):
    if Apple[i] + Pineapple[j] == Total_match:
      just += 1
      
print(just)
