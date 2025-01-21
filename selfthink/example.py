n = int(input())

a = str(n)
b = str(n)

if a == b[::-1]:
    print("Yes")
else:
    print("No")
