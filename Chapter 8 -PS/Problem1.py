def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c 
    
a=int(input("Ente the first Number "))
b=int(input("Enter the second Number "))
c=int(input("Enter the Third Number "))

print(f"The Greatest number  is {greatest(a,b,c)}")