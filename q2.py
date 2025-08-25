# 11. A user enters their name. Print their name in uppercase and lowercase using slicing
# only./

# name=input("Enter your name : ")

# print(name.upper())
# print(name.lower())

#12 A user enters a sentence. Print the first half and second half separately using slicing.

# strr=input("enter a sentance : ")

# print("First half is : ",strr[0:len(strr)//2])
# print("Second Half is : ",strr[len(strr)//2:])

#13 Take a number as input. If it is divisible by 5, print "Buzz", else print "Not Buzz".

# num=int(input("Enter a number : "))
# if num%5==0:
#     print("Buzz")
# else:
#     print("Not Buzz")

#14A user enters a password. Check if the password length is at least 8 characters. If yes,
# print "Strong", otherwise "Weak

# password=input("Enter a password : ")

# if len(password)>=8:
#     print("Strong password ")
# else:
#     print("weak password")
 


#15Input a string. If its first and last characters are the same, print "Match", otherwise "No
#Match"

# strr=input("Enter a string : ")

# if strr[0]==strr[len(strr)-1]:
#     print("Match ")
# else:
#     print("No match ")

#16A user enters marks (0–100). Print "Pass" if marks ≥ 33, else print "Fail".

# marks=int(input("Enter a marks : "))

# if marks>=33:
#     print("Pass")
# else:
#     print("Fail")

#17 Input a word. If the word is a palindrome (same forward and backward), print
# "Palindrome", otherwise "Not Palindrome".

# strr=input("Enter a String : ")

# if strr==strr[::-1]:
#     print("Palindrome")
# else:
#     print("No Palindrome")

#18 A user enters age. Print "Child" if age < 13, "Teenager" if 13–19, else "Adult".

# age=int(input("Enter your age : "))

# if age<13:
#     print("Child")
# elif 13<age<19:
#     print("Teenager")
# else:
#     print("Adult")
