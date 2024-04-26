import random as rand
import secrets
import string

# print(rand.randbytes(10))
# print(rand.random())

# print(s)

# print(secrets.token_bytes(10))

# print(rand.randrange(10))
# print(rand.randrange(1 ,10))
# print(rand.randrange(1 ,10 , 2))

# print(rand.randint(1, 10))

# print(rand.choice([1,2,3,4,5,6,7,8,9]))

# sample = [1,2,3,4,5,6,7,8,9]
# print(rand.shuffle(sample))

# # print(rand.sample([1,2,3,4,5,6,7,8,9], 5))
# print(rand.sample(['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] , 3))
s = rand.sample(['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] , 3)

print(s)
sa = ""
for a in s:
    sa = sa + a

print(sa)

# print(s[0])
# print(s[1])
# print("vsd")

# sa = "".join(rand.choices(string.ascii_lowercase, k=3))

# print(type(sa))
# print(str(sa))
