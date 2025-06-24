name=(input("enter your name : "))
age=int(input("enter your age : "))
height=float(input("enter your height :"))
python=bool(input("do u like python?(y/n)"))
subject=input("enter your favorite subjects : ".split(','))
dict={"name":name,"age":age,"height":height,"python":python,"subject":subject}
print("my name is "+name+" and i am ",age,"years old and my height is",+height,"and i like subjects like",subject)
print(dict)