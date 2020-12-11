4. Write a program to Print X Prime Numbers using While Loop starting from 0, and take the INput of X from the User 
Number = int(input(" Please Enter any Number: "))
count = 0
i = 2

while(i <= Number//2):
    if(Number % i == 0):
        count = count + 1
        break
    i = i + 1

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)