a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=str(input("Enter the operator: "))
if(c=='+'):
    print(a ,"+", b,"=",a+b)
elif(c=='-'):
    print(a ,"-", b,"=",a-b)
elif(c=='*'):
    print(a ,"*", b,"=",a*b)
elif(c=='/'):
    print(a ,"/", b,"=",a/b)
elif(c=='//'):
    print(a ,"//", b,"=",a//b)
elif(c=='%'):
    print(a ,"%", b,"=",a%b)
else:
    print("Wrong input")
