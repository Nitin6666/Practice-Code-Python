def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1) + n
n=int(input("Enter the Number "))
print(f"The sum of the Number is {sum(n)}")