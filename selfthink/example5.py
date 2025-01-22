l=list(map(int,input().split()))

t = int(input('target: '))

left = 0
right =0

for i in range(len(l)):
    if l[i] == t:
        print(i)
    elif t < l[i]:
        right = i - 1
    else:
        left = i + 1
    
print(left)
