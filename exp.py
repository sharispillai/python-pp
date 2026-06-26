try:
   a=int(input("enter the your number:"))
    b=0
    print(a/b)
except ZeroDivisionError: 
    print("you cannot divide a  number with zero")  
except ValueError:
    print("check your values")    
except TypeError:
    print("check your type")   
finally:
    print("This will always exceute!!! ")    
#assertion error
age=4
assert age>18,"age have to be greater"  
#raise   
name="Mohan"
if name!="hari": 
    raise Exception("name should be hari")