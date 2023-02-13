a=int(input("Enter the no:"))
i=int(0)
while a>10:
    a=a/3  #over here I am considering that decimal values are also significant
    #a=//3  if decimal values are not significant then we will use this 
    i=i+1
print(i)