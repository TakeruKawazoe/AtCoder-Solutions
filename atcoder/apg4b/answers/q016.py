wordnumber , over_wordlenge = map(int,input().split())
words = input().split()


result = [word for word in words if len(word) >= over_wordlenge]

print(*result)