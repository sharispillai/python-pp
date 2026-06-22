sm=lambda a,b,c,d,e:(a+b+c+d+e)/5
print(sm(1,2,3,4,5))
# squrae of a number
sq=lambda x:(x*x)
print(sq(5))
#square root of a number
sqrt=lambda x:(x**0.5)
print(sqrt(25))
#perimeter of a circle
cr=lambda r:(2*3.14*r)
print(cr(5))
#full name of a person
full=lambda fname,mname,lname:fname+mname+lname
print(full("mohan","das","gandhi"))
#check if a person is eligible for vote for not 
vote=lambda age:"eligible" if age>=18 else"not eligible"
print(vote(21))



