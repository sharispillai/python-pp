def add(x,y):
       return x+y
def subtract(x,y):
       return x-y
def multiply(x,y):
         return x*y
def divide(x,y):
       return x/y 
print("welcome to the calculator")
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
choice=(int(input("enter your choice:1.add\n2.subtract\n3.multiply\n4.divide\n5.exit")))
if choice==1:
    print(add(x,y))
elif choice==2:
     print(subtract(x,y))
elif choice==3:
     print(multiply(x,y))
elif choice==4:
     print(divide(x,y))   
else:
   print("invalid choice")    

  
     