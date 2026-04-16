A, op, B = input().split()
A = int(A)
B = int(B)
 
if op == "+":
    print(A + B)
elif op == "-":
    print(A - B)
elif op == "*":
    print(A * B)
elif op == "/" and B != 0:
    print(A // B)
else:
    print("error")