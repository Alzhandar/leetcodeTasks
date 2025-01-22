l=list(map(int,input().split()))
l2 = len(l)
val = int(input())

l = [x for x in l if x != val]


dif_count = l2 - len(l)

for i in range(dif_count):
    l.append('_')


print(dif_count)

print(l)