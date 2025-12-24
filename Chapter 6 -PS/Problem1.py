a=int(input("Enter first Number "))
b=int(input("Enter second Number "))
c=int(input("Enter third Number "))
d=int(input("Enter fourth Number "))

if(a>b and a>c and a>d):
    print("Greater number is first ",a)
elif(b>a and b>c and b>d):
    print("Greater Number is second ",b)
elif(c>a and c>b and c>d):
    print("Greater Number is third ",c)
elif(d>a and d>b and d>c):
    print("Greater Number is fourth ",d)