N = int(input()) #計算する回数
A = int(input()) #最初に受け取る数字

for i in range(N):# N(計算する回数)の数だけ演算子(s)と数字(n)を受け取る
  s,n = input().split()
  n = int(n) # nをint型に変換
  
  if s == "+":
    A = A+n
  elif s == "-":
    A = A-n
  elif s == "*":
    A = A*n
  elif s == "/" and n != 0:
    A = A//n
  else: #割る数が0だった場合はエラーを吐いてbreak文で抜け出す
    print("error")
    break
  
  
  print(i+1,A) #何回目の計算なのか、計算した数