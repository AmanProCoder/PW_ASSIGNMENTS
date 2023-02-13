a=1
while a<4:
    b=a
    print("Pattern ",a,":")
    while b>0:
        print(" "*(a-b)+"*"*b*2)
        b=b-1
    a=a+1
