l = list(map(int,input().split()))

l2 = []
l.sort()

for i in range(len(l)+1):
    l2.append(i)

print(l)
print(l2)

missing = list(set(l2) - set(l))


print(missing[0])
