l = [0,0,0]
l[0] = int(input("What is answer of 1st question:\n 5 + 7 = "))
l[1] = int(input("What is answer of 2nd question:\n 2 + 3 = "))
l[2] = int(input("What is answer of 3rd question:\n 7 + 9 = "))

if l[0] == 12 and l[1] == 5 and l[2] == 16:
    print("You are correct in 3 out of 3 questions \n so you won 3 lakh rupees") 
    
elif (l[0] == 12 and l[1] == 5) or (l[0] == 12 and l[2] == 16) or (l[1] == 5 and l[2] == 16):
    print("You are correct in 2 out of 3 questions \n so you won 2 lakh rupees") 
    
elif (l[0] == 12) or (l[1] == 5) or (l[2] == 16):
    print("You are correct in 1 out of 3 questions \n so you won 1 lakh rupees")
    
else:
    print("You are wrong \n so you are won 10k rupees")
    
    print("Thanks for playing")