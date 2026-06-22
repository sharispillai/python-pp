def countozero(n):
    print(n)
    if n==0:
       return
    return(countozero(n-1))
countozero(10)
#sum of first 10 number using recursion
def countozero(n):
    if n==0:
        return 0
    return n + countozero(n-1)
print(countozero(10))
#factorial of a number using recursion
def factorial(n):
    if n==1:
     return 1
    return n*factorial(n-1)
print(factorial(5))
#non recursion area 
# print vowels and their index from a string
name="mohan"
for i in range(0,len(name)):
   if name[i]=="a"or name[i]=="o"or name[i]=="i"or name[i]=="u"or name[i]=="e":
    print(i,name[i])


  