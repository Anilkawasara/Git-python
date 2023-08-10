#day 3 Regex
for i in range(1,100,5):
  print(i)

str = input("enter the number")
words = str.split()
for word in words:
    if(word[::]==word[::-1]):
        print("word reverse",word)
    else:
        print("word not reverse")
 
num = input("enter the number")
print(num[4])

num = input("enter the number")
print(len(num))

#lenth of word
num = input("enter the number")
for n in range(len(num)):
    print(num[n])
    
str = input("enter the number")
for word in range(len(str)):
        if word%2==0:
            print("even",str[word])
            
#day 4 regex

#nested loop
for i in range (0,5):
     for j in range(0,5):
         print(i , end = "")
     print("\n")
         
for i in range(0,10):
    for j in range(0,10-i):
        print("*", end = "" )
    print("\n")
    
for i in range(0,5):
    for j in range(0,5-i):
        print(end=" ")
        
    for k in range(0,i+1):
        print("*",end="")
    print("\n")
    
for i in range(0,5):
    for j in range(0,5):
        if (i==0 or i==4 or j==0 or j==4):
            print("*",end=" ")
        else:
            print(end=" ")
    print("\n")


 0 1 2 3 4 5 6  
0* * * * * * *
1*           *
2*           *
3*           *
4*           *
5*           *
6* * * * * * *
n=14
        
for i in range(0,n):
    for j in range(0,n):
        if (j==0 or j==n-1 or (i-j==0 and i<(n/2)) or( i+j==n-1) and i<n/2 ):
            print("*", end = "")
        else:
            print(end =" ")
            
    print("\n")
    
#Day 5 Regex

#array in python
a = 10
b = 20
c = 30
d = 80
if(a>b):
    if(a>c):
        if(a>d):
            print("a is greater")
        else:
            print("d is greater")
    else:
        print("c is greater")
elif(b>c):
    if(b>d):
        if(b>a):
            print("b is greater")
        else:
            print("a is greater")
    else:
         print("b is greater")
elif(c>d):
    if(c>a):
        if(c>b):
            print("c is greater")
        else:
            print("b is greater")
    else:
        print("a is greater")
else:
    if(d>a):
        if(d>b):
            print("d is greater")
        else:
            print("b is greater")
    else:
        print("a is greater")
        
#Array in python
#(1) list
#(2) tuple
#(3) set
#(4) dictenerry

#list
a = [20,30,40,50,"Anil"]
print(a)

#append
a = [10,20,30,40,"Anil"]
a.append("Ashok")
#a.pop()
print(a)