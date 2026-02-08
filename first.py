print("k" in "key")
l=int(input("Enter a number:"))
b=int(input("Enter another number:"))
area= l*b
print("The area is :" ,area)
print("the area of the square is :" , b*b)
print("the area of circle is :" , 3.14*b*b)
remainder= l%b
print(remainder)

celcius= float(input("Enter the temperature in Celcius:"))
fahrenheit= (celcius*9/5) + 32
print(fahrenheit)

principle = float(input("Enter the principle:"))
rate = float(input("Enter the rate:"))
time=float(input("Enter the time:"))
simpleInterest =principle*rate*time
print(simpleInterest)

char = input("Enter a character:")
if char.lower() in ['a','e','i','o','u']:
    print("vowel")
else :
    print("consonant")


math = int(input("ENTER THE MARKS OF MATH"))
PHYSICES = int(input("ENTER THE PHYSICES"))
chemistry = int(input("ENTER THE CHEMISTRY"))
english = int(input("ENTER THE ENGLISH"))
hindi = int(input("ENTER THE HINDI"))
total = math + PHYSICES + chemistry + english + hindi
print(total)
percentage = total /5
print(percentage)
if percentage >= 75 :
   print("grade A")
elif percentage >= 60 :
   print("grade B")
elif percentage >= 45 :
   print("grade C")
else :
   print("TRY AGAIN")


#TABLE OF ANY NUMBER
n = int(input("enter any number that you want to table :"))
for i in range(n,10*n+1,n):
   print(i)


#"OR"
for i in range(1,11,1):
   print(n*i)

 # PRINT ANY NATURAL NUMBER
n = int (input ("enter the number :"))
for i in range(1,n+1,1):
 print(i)

# EXAMPLE USING WHILE LOOP
# PRINT N NATURAl NUMBER
n = int(input("Enter a number: "))
i = 1
while i <= n:
   print(i)
   i+= 1

#  INVERSE OF N NATURAL NUMBER
n = int(input("Enter a number: "))
i = n
while i>= 1:
   print(i)
   i+=1



for i in range(1,11,1):
   if i == 6:
       break
   print(i)


# sum of  n natural number
sum = 0
for i in range(1,10,1):
   print(i)
   sum += i
print(sum)


#  sum of  multiple of n number
n = int(input("Enter a number: "))
sum = 0
for  i in range(n):
   number = float(input("Enter a number{i+1}: "))
sum += number
print(sum)


