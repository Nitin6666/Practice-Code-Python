s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations
print(len(s))
#In python the 20.0 and 20 is considered as the same number and also the set does not store the same values this is why the output is 2 