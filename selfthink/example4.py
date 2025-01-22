# s1 = input('haystack = ')
# s2 = input('needle = ')

# l = []

# for i in range(0, len(s1)):
#     if s1.find(s2, i):
#         l.append(i)
#         print(l)
#     else:
#         print(-1)
#         break
def printIndex(str, s):

    flag = False
    for i in range(len(str)):
        if (str[i:i + len(s)] == s):

            print(i, end=" ")
            break
        else:
            print(-1)
            break


# Driver code
# str1 = "leetcode"
# str2 = "leeto"

str1 = "sadbutsad"
str2 = "sad"
printIndex(str1, str2)

