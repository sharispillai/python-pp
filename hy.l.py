a=[1,2,3,4,5,3,2,1,6,7,8,5,6,7,9,10]
result=[]
for i in a:
 if a not in result:
  result.append(i)
print(result)  
#swapping
a=3
b=7
temp=a
b=a
b=temp
print("a=",a)
print("b=",b)
#without using a third variable 
a=5
b=7
a=a+b
b=a-b
a=a-b
#split the list into two list
a=[11,12,13,14,15,16,17,18,19,20]
list1=a[:5]
list2=a[5:]
print("list1:",list1)
print("list2:",list2)
#another way to split the list
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=[]
mid=len(a)//2
for i in range (len (a)):
    if i<mid:
     b.append(a[i])
    else:
      c.append(a[i]) 
print(b)
print(c)      
  