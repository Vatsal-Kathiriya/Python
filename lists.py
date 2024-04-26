l = [1,2,3,4,5,6,7,8,9]

print(l)

m = l
print(m)

m[0] = 34
print("This is m " , m)
print("This is l " , l)

s  = l.copy()
s[0] = 44
print("This is s " , s)
print("This is l " , l)

print(l[-9])

l.append(43)
print(l)