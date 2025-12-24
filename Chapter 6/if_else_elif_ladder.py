#if-elif-else Ladder 
age=int(input("Enter the Age "))
if(age>=18):
    print("You are eligible ")
elif(age==0):
    print("You have entered 0 which is not valid ")
elif(age<0):
    print("You are entering negative age which is not valid ")
else:
    print("You are not eligible")
#Multiple if state are allowed in python but multiple elif and else statement are not allowed until they will fall under the if _ elif _ else ladder 