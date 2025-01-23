l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

set1 = set(l1)
set2 = set(l2)

print(list(set1.intersection(set2)))