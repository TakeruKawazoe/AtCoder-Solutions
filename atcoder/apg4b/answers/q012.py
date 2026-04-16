SN = [] 
Time=[]

SN = int(input())
Time = list(map(int,input().split()))
#一番数字が小さいやつを選ぶ
fast = min(Time)

#そいつが何番目かを出力する
for i,v in enumerate(Time):
  if v ==fast:
    print(i+1)
    break