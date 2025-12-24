m1=int(input("Enter Marks "))
m2=int(input("Enter Marks "))
m3=int(input("Enter Marks "))
total_percentage=(100*(m1+m2+m3)/300)
if(total_percentage>=40 and m1>33 and m2>33 and m3>33):
    print("You have passed the exam !")
else:
    print("You was failed ")
    