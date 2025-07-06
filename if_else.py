# 53. WAP to check whether a number is positive or negative. If Positive print positive
# message or else print Negative Number.

# n = int(input("Enter the num : "))
# if (n>0):
#     print("positive")
# else:
#     print("negative")





# 54. WAP to check whether a number is even or odd. If even, print message an even or
# else print message as odd.

# n=int(input("Enter the num : "))
# if (n%2==0):
#     print("EVEN")
# else:
#     print("ODD")
    


# 55. Write a program to check whether a given number is greater than 10 or not. if it is
# greater than 10 print message as greater or else print that number with not a greater
# than.

# n=int(input("no : "))
# if (n>10):
#     print("number greater that 10")
# else:
#     print("not greater than 10")
    



# 56. WAP to check whether a given value is present in between 45 to 125. If value is
# present print the ascii character.

# n= int(input("enter the value : "))
# if (n>45 and n<125):
#     print(chr(n))
# else:
#     print("invalid")




# 57. WAP to check whether the given two input numbers are divisible by 3 and 5. If it is
# divisible, print “Good Morning”, if it is not print “Good Evening”.

# n1 = int(input("enter the 1st num : "))
# n2 = int(input("enter the 2nd num : "))
# if(n1%15==0 and n2%15==0):
#     print("good morning")
# else:
#     print("good evening")



# 58. WAP to accept two integers and check whether they are equal or not.
# If equal, multiply to value or quotation value and display it.

# a = int(input("enter 1st num : "))
# b = int(input("enter 2nd num : "))
# if(a==b):
#     print(a*b)
# else:
#     print('a*b')




# 59. WAP to find the largest of two numbers.

# n = int(input("enter the num : "))
# n2 = int(input("enter the 2nd num : "))
# if(n>n2):
#     print(n," is the larger num")
# else:
#     print(n2," is the larger num")




# 60. WAP to check whether the input number is greater than 10 or not if it is greater than
# 10 print messages as greater with print that number. if that number is not greater
# than 10 print that number.

# n = int(input("input number"))
# if(n>10):
#     print(n," is the greater than 10")
# else:
#     print(n)




# 61. WAP to the given number integer, if n is greater than 21,print the absolute
# difference between n and 21 otherwise print twice the absolute difference.

# n=int(input("enter the number : "))
# if (n>21):
#     print(abs(n-21))
# else:
#     print(2*(abs(n-21)))
    


# 62. WAP to find the smallest of two numbers.

# a=int(input("enter the number : "))
# b=int(input("enter the number : "))
# if(a>b):
#     print(b," is the smaller of the two.")
# else:
#     print(a,"is the smallest of the two.")




# 63. WAP to check whether the given number is even or odd. If it is even then make it as
# an add number, if it is an odd number then make it as even number.

# n = int(input("enter the number : "))
# if(n%2==0):
#     print(n+1)
# else:
#     print(n+1)




# 64. WAP to check whether the given number is divisible by 3 or not if yes,print the
# number or else print the cube of the numbers.

# n= int(input("enter the numb"))
# if(n%3==0):
#     print(n)
# else:
#     print(n**3)




# 65. WAP to check whether the given input is divisible by 3 and 5. If yes print the actual
# number or else print string of that number.

# n= int(input("enter the num : "))
# if(n%15==0):
#     print(n)
# else:
#     print(str(n))




# 66. WAP to check whether the given number lies between 1 to 19, if it is true square that
# number or else false cube that number and display the number.

# n = int(input("enter the number : "))
# if(n>=1 and n<=19):
#     print(n**2)
# else:
#     print(n**3)




# 67. WAP to check whether the student has passed or failed. If the student got more than
# 40 marks, print ‘PASS’ along with those marks, if it is not printed ‘FAIL’ along with
# those marks.


# marks= int(input("enter the marks : "))
# if(marks>40):
#     print("PASS , with mark ",marks)
# else:
#     print("failed , with mark ",marks)



# 68. WAP to check whether a given value is even and in range of 47 to 58 and not in 0 or
# odd. if condition is True, to perform display the ascii character.or else to perform
# floor division with 5 and display it.

# n= int(input("enter the number : "))
# if ( (n%2==0) and (n>=47 and n<=58) and (n!=0)):
#     print(chr(n))
# else:
#     print(n//5)




# 69. WAP to check whether a given value is less than 125 and in between 47 to 125 or not.
# if condition is True, to perform store the given value as key and value as a character
# into the dict.or else to append the value in list and display it.

# n = int(input("enter the number : "))
# if(n>=47 and n<=125):
#     dict1={n:chr(n)}
#     print(dict1)
# else:
#     print([n])




# 70. WAP to check whether a given character is in the alphabet or not. if alphabet,
# display the alphabet with character.or else display the not alphabet with character.

# n=input("enter the character : ")
# if(n>='a'and n<='b') and (n>='A'and n<='B'):
#     print("ITS ALPHABET")
# else:
#     print("ITS NO ALPHABET")




# 71. WAP to check whether a given character is uppercase or other character. if
# uppercase, display the uppercase with character.or else display the other character
# with character.

# n = input("enter the number : ")
# if (n>='A'and n<='B'):
#     print("uppercase ",n)
# else:
#     print("other character ",n )





# 72. WAP to check whether a given character is lowercase or other character. if
# lowercase, display the lowercase with character.or else display the other character
# # with character.

# n = input("enter character : ")
# if(n>='a' and n<='z'):
#     print(n,"lower character")
# else:
#     print(n)




# 73. WAP to check whether a given character is uppercase or other character. if
# uppercase, convert to lowercase .or else display the ascii number.

# n = input("enter the character : ")
# if(n>='A' and n<='Z'):
#     l=ord(n)
#     print(chr(l+32))
# else:
#     print(ord(n))



# 74. WAP to check whether the given character is in lowercase or uppercase. If it is in
# lowercase, convert it into uppercase, or else it is in uppercase and convert it into
# lowercase. Display the value.

# ch = input("Enter the character : ")
# l2=ord(ch)
# if(ch>='a' and ch<='z'):
#     print("it was in lower converted to upper ", chr(l2-32))
# else:
#     print("it was in upper converted to lower ",chr(l2+32))



    
# 75. WAP to check whether the given string of the first character is a special symbol or
# not. If a special symbol, to extract and display the middle character or else to
# reverse the string and display the half of the string.

# n = input("enter the character : ")
# length=len(n)
# mid=length//2
# f1=n[0]
# if (ord(f1)>=32 and ord(f1)<=47):
#     print(n[mid])
# else:
#     print(n[ : :-1])




# 76. WAP to check whether the input character is a vowel or not. If it is vowel print
# ‘VOWEL’ along with that character, if it is not just print ‘CONSONANT’.

# ch = input("enter the character : ")
# vowel = "AEIOUaeiou"
# if(ch in vowel):
#     print('VOWELS : ',ch)
# else:
#     print("CONSONANTS : " ,ch)




# 77. WAP to check whether a given character is a vowel or consonant. if vowel,to print
# the next character of a given character or else print previous characters.

# ch=input("enter the character : ")
# vowels="AEIOUaeiou"
# l1=ord(ch)
# if(ch in vowels):
#     print(chr(l1+1))
# else:
#     print(chr(l1-1))




# 78. WAP to check whether a given string of first character is alphabet or not
# if the alphabet prints, reverse the string or else print the middle character.
   
# ch=input(" enter the string : ")
# f1=ch[0]
# mid=len(ch)//2
# if(f1>='A'and f1<='B') or (f1>='a'and f1<='z'):
#     print(ch[ : : -1])
# else:
#     print(ch[mid])
 



# 79. WAP to check whether the given input character is uppercase or lowercase. If the
# input character is upper case convert into lower case and vice versa.

# ch = input("Enter the character : ")
# l2=ord(ch)
# if(ch>='a' and ch<='z'):
#     print("it was in lower converted to upper ", chr(l2-32))
# else:
#     print("it was in upper converted to lower ",chr(l2+32))




# 80. WAP to check whether a given string is less than 3 characters, to print the entire
# string otherwise to print after third positions to the remaining string.

# st = input("enter the string : ")
# length=len(st)
# if(length<3):
#     print(st)
# else:
#     print(st[2])



# # 81. WAP to check whether a given length of the string is even or not. if even, to append
# # the new string called "bye" or else print the first and last characters.

# s=input("enter the string : ")
# if len(s)%2==0:
#     print(s+"bye")
# else:
#     print(s[0]+s[-1])





# # 82. WAP to check whether a given length of the string is odd or not. if odd, to append
# # the new string("Haii") from the starting of the given string, or else to avoid the
# # starting character and ending character of the given
# # string and to display the remaining characters.

# s=input("enter the string : ")
# if len(s)%2!=0:
#     print("Haii"+s)
# else:
#     print(s[1:-1])




# # 83. WAP to check whether the last of the given string is a special character or not, if the
# # special character prints reverse the string except the last character or else to check
# # if the length of the string is odd or not, if odd to extract the middle character to the
# # end of the string.

# s=input("enter the string : ")
# last=s[-1]
# if ord(last)>=32 and ord(last)<=47:
#     print(s[:-1][::-1])
# elif len(s)%2!=0:
#     print(s[len(s)//2:])






# # 84. WAP to check whether a given year is a leap year or not. if leap year, print leap year
# # or else not a leap year.

# y=int(input("enter year : "))
# if (y%4==0 and y%100!=0) or (y%400==0):
#     print("leap year")
# else:
#     print("not a leap year")



# # 85. WAP to find out the greatest of two numbers and display the greatest number.if the
# # greatest number, display the greatest message with value.

# a=int(input("enter 1st num : "))
# b=int(input("enter 2nd num : "))
# if a>b:
#     print("greatest number is",a)
# else:
#     print("greatest number is",b)





# # 86. WAP to check whether the given value is present inside the given collection or not.if
# # value is present, display the value is available or else the value is not present.

# val=input("enter value : ")
# coll=input("enter comma values : ").split(",")
# if val in coll:
#     print("value is available")
# else:
#     print("value is not present")





# # 87. WAP whether a given string, if string length is more than 2, then it displays a new
# # string with the first and last characters switched, otherwise the display the 3 copies
# # of given string.

# s=input("enter the string : ")
# if len(s)>2:
#     print(s[-1]+s[1:-1]+s[0])
# else:
#     print(s*3)





# # 88. WAP to check whether a given value is a list and first and last values should be
# # integer,if condition is satisfied first value is true division by 3 and perform the
# # bitwise not for last value and those result values are stored in same positions in list
# # or else, to perform length of the collection power 2 and display it.

# l=input("enter values : ").split()
# if (ord(l[0][0])>=48 and ord(l[0][0])<=57) and (ord(l[-1][0])>=48 and ord(l[-1][0])<=57):
#     l[0]=str(int(l[0])/3)
#     l[-1]=str(~int(l[-1]))
#     print(l)
# else:
#     print(len(l)**2)


# # 89. WAP to check whether a given value is a string or not and length of the value should
# # be more than 7, if condition is satisfied to append the new string in the middle of the
# # given string or else to perform the replications with 3 and display the result.

# s=input("enter value : ")
# if (ord(s[0])>=65 and ord(s[0])<=90) or (ord(s[0])>=97 and ord(s[0])<=122) and len(s)>7:
#     m=len(s)//2
#     print(s[:m]+"new"+s[m:])
# else:
#     print(s*3)


# # 90. WAP to check if the given string of first and second character should be sequence or
# # not. if the sequence prints the first,second and last two characters, or else the first
# # half string is reversed and the remaining half string should be normal and display it.


# s=input("enter string : ")
# if ord(s[1])-ord(s[0])==1:
#     print(s[0]+s[1]+s[-2]+s[-1])
# else:
#     h=len(s)//2
#     print(s[:h][::-1]+s[h:])





# # 91. WAP to check whether a given value is present inside the collection or not. If
# # present, print the value or else print value is not found.


# v=input("enter value : ")
# c=input("enter collection : ").split()
# if v in c:
#     print(v)
# else:
#     print("value is not found")






# # 92. WAP to check whether a given key is present in the dict or not. if key is present:
# # display the value or else add key and new value inside the dict.

# d = {"a":1,"b":2}
# k = input("enter key : ")
# if k in d:
#     print(d[k])
# else:
#     v = input("enter value : ")
#     d[k] = v
#     print(d)





# # 93. WAP to check whether a given collection is set or not.if set, append the new value,
# # or else eliminate the duplicate values in collection. final results should be set type.

# val=input("enter space values : ").split()
# if type(set(val))==set:
#     val.append("new")
#     print(set(val))
# else:
#     print(set(val))





# # 94. WAP to read the age of a candidate and determine whether it is eligible for his/her
# # own vote or not.it eligible print age and eligible messages or else print not eligible.

# age=int(input("enter age : "))
# if age>=18:
#     print("eligible with age ",age)
# else:
#     print("not eligible")




# # 95. WAP to check whether a given value is even and in between 47 to 58 and not in 0 or
# # odd. if condition is True, to perform display the ascii character.or else to perform
# # floor division with 5 and display it.

# n=int(input("enter number : "))
# if (n%2==0) and (n>=47 and n<=58) and (n!=0):
#     print(chr(n))
# else:
#     print(n//5)


# # 96. WAP to check whether the given string is palindrome or not if it is a palindrome
# # string palindrome along with the string if it is not a palindrome print not palindrome

# s=input("enter string : ")
# if s==s[::-1]:
#     print("palindrome",s)
# else:
#     print("not palindrome")





# # 97. WAP to check whether a given number is palindrome or not. If palindrome, display
# # the given value as a palindrome or else not a palindrome.


# n=input("enter number : ")
# if n==n[::-1]:
#     print("palindrome",n)
# else:
#     print("not palindrome")


# # 98. WAP to check length of both string collections equal or not if both are equal print
# # the concat the two strings and display, or else if any one of the collection not equal
# # print both the collections with lengths

# a=input("enter first string : ")
# b=input("enter second string : ")
# if len(a)==len(b):
#     print(a+b)
# else:
#     print(a,len(a))
#     print(b,len(b))

  


# # 99. WAP to check whether both given values point to the same memory location or not.
# # if it is true print the middle item of the second collection, or else if it is false print the
# # first item and last item of the first collection along with the memory address.


# x=input("enter value 1 : ")
# y=input("enter value 2 : ")
# if x is y:
#     print(y[len(y)//2])
# else:
#     print(x[0],x[-1],id(x))

# # 100. WAP to check whether a given string collection is more than ten, and the first + last
# # character of the ascii values should be divisible by 5, if condition is satisfied print
# # first,middle,last characters ASCII values or else print the string three times.

# s=input("enter string : ")
# if len(s)>10 and (ord(s[0])+ord(s[-1]))%5==0:
#     print(ord(s[0]),ord(s[len(s)//2]),ord(s[-1]))
# else:
#     print(s*3)






# # 101. WAP to check whether the middle of the item present in the list is string data type or
# # not if it is string print that list or else if it is not string then print that middle item.

# l=input("enter list values : ").split()
# m=l[len(l)//2]
# if (ord(m[0])>=65 and ord(m[0])<=90) or (ord(m[0])>=97 and ord(m[0])<=122):
#     print(l)
# else:
#     print(m)


# # 102. WAP Given a string, return a new string where the first and last characters have
# # been exchanged.

# s=input("enter string : ")
# if len(s)>1:
#     print(s[-1]+s[1:-1]+s[0])
# else:
#     print(s)





# # 103. Write a program to find out such numbers which are divisible by 7 but are not a
# # multiple of 5. Both the conditional are satisfied and print actual value. if one
# # condition is not satisfied actual number is multiply by 4 and print result

# n=int(input("enter number : "))
# if n%7==0 and n%5!=0:
#     print(n)
# else:
#     print(n*4)




# # 104. WAP to check whether two values are pointing to the same memory address or not.
# # If the same memory displays the address or else displays the two values addresses.

# a=input("enter 1st value : ")
# b=input("enter 2nd value : ")
# if a is b:
#     print(id(a))
# else:
#     print(id(a),id(b))


# # 105. WAP to check whether a given input character is a special symbol or not if it is a
# # special symbol then print that character three times and tell print that character 5
# # times.


# ch=input("enter character : ")
# if ord(ch)>=32 and ord(ch)<=47:
#     print(ch*3)
#     print(ch*5)





# # 106. WAP to check length of both string collections equal or not if it is equal print the
# # connection of any one of the collections if it is not equal print both the collection.


# a=input("enter string a : ")
# b=input("enter string b : ")
# if len(a)==len(b):
#     print(a)
# else:
#     print(a)
#     print(b)



# # 107. WAP To check whether both input variables point to the same memory location or
# # not if it is true print the last item of the second collection, if it is false print the first
# # item of the first collection along with the memory address.

# a=input("enter 1st list val : ")
# b=input("enter 2nd list val : ")
# if a is b:
#     print(b[-1])
# else:
#     print(a[0],id(a))





# # 108. WAP to print the string collection five times when the length of the string collection
# # should be more than 3 and the middle character of the string should be vowel and
# # the first character ASCII value should be even, to print the previous character of
# # middle character, or else if ASCII value is odd then print the string three times as
# # print that string.

# s=input("enter string : ")
# m=s[len(s)//2]
# if len(s)>3 and m in "aeiouAEIOU":
#     if ord(s[0])%2==0:
#         print(chr(ord(m)-1))
#     else:
#         print(s*3)





# # 109. Ravi would like to buy a new cello or red pen. The cost of the pen should be 10. If
# # the pen is available in the shop, he will buy the pen. If it is not there he will come out
# # of the shop.

# c=int(input("enter cost : "))
# a=input("pen available yes or no : ")
# if c==10 and a=="yes":
#     print("Ravi buys pen")
# else:
#     print("Ravi leaves")





# # 110. WAP to perform addition and subtraction operation by using list collection if the first
# # and middle data items number are even performing addition operation, or else
# # performing subtraction.

# l=input("enter list values : ").split()
# a=int(l[0])
# b=int(l[len(l)//2])
# if a%2==0 and b%2==0:
#     print(a+b)
# else:
#     print(a-b)




# # 111. WAP to check whether the first item of these two lists is either integer or not. If
# # it is an integer, concatenate these two lists or else print the memory address of
# # these two lists.

# a=input("enter list a : ").split()
# b=input("enter list b : ").split()
# if (ord(a[0][0])>=48 and ord(a[0][0])<=57) and (ord(b[0][0])>=48 and ord(b[0][0])<=57):
#     print(a+b)
# else:
#     print(id(a),id(b))

