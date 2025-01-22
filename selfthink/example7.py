l=list(map(int,input().split()))

num = 0
for i in range(len(l)):
    num += l[i] * 10 ** (len(l) - i - 1)

print(num+1)