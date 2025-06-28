l1=[0,1,2,3,4,5,6,7,8,9]
target=9

for i in range(0,len(l1),1):
    for j in range(i+1,len(l1)):
        if(l1[i]+l1[j]==target):
            print("found at indices",i,j)