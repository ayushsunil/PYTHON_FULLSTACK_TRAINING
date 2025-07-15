n=int(input(" enter the number : "))
while(n>9):
    sum=0
    num=0
    while(n>0):
        dig=n%10
        sum+=dig
        n=n//10
        num=sum
    if(num<9):
      print("final sum",sum)  
    else:
        n=sum
        print("Intermediate Sum",sum)

