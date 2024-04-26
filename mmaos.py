def hey(lisst):
    sum = 0;
    for a in lisst :
        sum = sum + a
    print(sum)
    
    avg = sum / len(lisst)
    print(avg)
    
sibli = [1,2,3,4,5,6,7,8,9,10]

hey(sibli)

s = map(lambda x : x + 1 , sibli)

print(list(s))
# sib = int(input("Enter a sibling : "))
sib = []
for a in sibli :
    print(a + 1,end=" ")
    
    sib.append(a + 1)

print()
print(sib)


# print("Vatsal Kathiriya")
# print("Harsh Vekariya")
# print("Vatsal Kathiriya")