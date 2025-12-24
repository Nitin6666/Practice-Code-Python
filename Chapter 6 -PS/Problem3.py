s1="Make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"
post=input("Enter the post : ")
if((s1 in post ) and (s2 in post ) and (s3 in post) and (s4 in post)):
    print("This is a scam comment ")
else:
    print("This is not a scam comment ")