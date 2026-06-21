
print("welcome to the calculator")
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
choice=(int(input("enter your choice:1.add\n2.subtract\n3.multiply\n4.divide\n5.modulus\n6.floor division\n7.exit\n")))
if choice==1:
    print(x+y)
elif choice==2:
     print(x-y)
elif choice==3:
     print(x*y)
elif choice==4:
     print(x/y)
elif choice==5:
     print(x%y)
elif choice==6:
     print(x//y)        
else:
   print("invalid choice")    
