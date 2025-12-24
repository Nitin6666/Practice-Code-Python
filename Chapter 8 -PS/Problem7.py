def rem(l,word):
    n=[]
    for item in l:
        if not(word==item):
            n.append(item.strip(word))
    return n
l=["harry","Nitin","larin","in"]
print(rem(l,"in"))