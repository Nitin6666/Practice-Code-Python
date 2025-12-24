letter = ''' Dear <|Name|>, 
You are selected! 
<|Date|>'''
name=input("Enter the Name ")
print(letter.replace("<|Name|>",name).replace("<|Date|>","17 December 2025"))