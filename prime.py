num=int(input("enter the number:-"))
prime=True
if num==1:
  prime==False
else:
  for i in range(2,num):
    if num % i==0:
      prime=False
      print("not a prime")
      break    
    else:
      print("prime")