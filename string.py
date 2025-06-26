# 🧠 Easy
# Ask user for their name, and greet them in uppercase.

# Check if a user-given word is a palindrome.

# Ask for a sentence and count how many words are in it.

# ⚔️ Medium
# Reverse a string using slicing and loop.

# Replace all spaces in a sentence with -.

# Count vowels and consonants in a string.

# 💡 Mini Project Idea
# Would you like to build a:

# 🔒 Password Strength Checker?

# 📧 Email Validator?

# 🧼 String Cleaner Utility?

# Or should I now move to functions in Python?




#EASY
#_________________________________________
# name=input("What is your name? ")
# print("hello",name.upper(),"!")
#_________________________________________

#PALINDROME
# word=input("Enter a word: ")
# if word ==word[ : :-1] :
#     print("the word is palindrome")

# else:
#     print("not a palindrome")
#_________________________________________

#word count
# sentence = input("enter the sentence:")
# list=sentence.split( )
# print(len(list))

#_____________________________________________



#reverse a string

# original_string = input("enter the string : ")
# reverse_string = original_string[ : :-1]
# print("the reversed string : ",reverse_string)

#_____________________________________________

# replace space with _

# sentence=input("Enter the sentence : ")
# print(sentence.replace(" ","_" ))

#_____________________________________________
#count the number of vowles and consonants


word=input("enter the word : ")
vowel="aeiouAEIOU"
vowels=0
consonants=0
for char in word :
    if  char.isalpha():
        if char in vowel :
            vowels+=1
        else:
            consonants+=1

print("number of vowels: ",vowels )
print("number of comnsonants : ",consonants)
            