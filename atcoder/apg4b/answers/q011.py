S = input()

answer = 1

for  i in range(len(S)):
  if S[i] == "+":
    answer += 1
  elif S[i] == "-":
    answer -= 1
  else:
    continue
    
print(answer)