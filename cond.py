a=int(input("enter marks for maths :"))
b=int(input("enter marks for physics :"))
c=int(input("enter marks for chemistry :"))
total_marks=a+b+c
print("total marks : ",total_marks)
percentage=(total_marks/300)*100
print("percentage : ",percentage)
if(percentage>=95):
    print("GRADE S")
elif(percentage>=90):
    print("GRADE A")
elif(percentage>=80):
    print("GRADE B")          
else:
    print("GRADE C")                                              