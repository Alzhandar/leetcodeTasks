n = int(input())

l = []
c = 0
for i in range(n):
    l.append(input())
    c += 1
print("Size of list", c)


l2 = sorted(list(set(l)))
l3 = list(l2)

c2 = c - len(l2)
print(c2)

for i in range(c2):
    l3.append("_")


print(f'{c2}, nums = {l3}')