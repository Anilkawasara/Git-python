for i in range (1,101):
    print(i)
    
i = 1 
while(i<=100):
   print(i)
   i = i+1
    
a = int(input("enter the number"))
i=1
while i<=a:
  print(i)
  i = i+1
    
i=1
while i<=100:
    if(i%2==0):
        print("even",i)
    else:
        print("odd",i)
    i=i+1
#table of n
num = int(input("enter the number"))
for i in range(10):
    print(f"{num}x{i}={num*i}")
    
# (1)find the factorial
num = int(input("enter the value"))
fact=1

# (2) freuency of digit in an integer
for i in range(1,num+1):
    fact=fact*1
    i=i+1
    print(fact)
 
# (3) write a program to reverse number
num = input("enter the value")
print(num[::-1])

#(4) sum of digit number
num = input("enter the value")
add=0
for i in str(num):
   add+=int(i)
   print(add)
    
#(5)print alphabet  a to 


#(6)find first and last number
num = input("enter the value")
print("first number",num[0],"last number",num[-1])