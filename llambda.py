x = int(input("Enter a number x : "))
y = int(input("Enter another number y : "))



# squares = lambda x : x*x

# print(squares(x))

# cubes = lambda y : y*y*y

# print(cubes(y))


# def myfunc(squares , cubes , x , y):
#     return squares(x) + cubes(y)

# print(myfunc(squares , cubes , x , y))

def myfunc2(squares , cubes):
     return squares(x) + cubes(y)

print(myfunc2(lambda x : x*x , lambda y : y*y*y ))

