import math
print("Select 1 for addtion\n"
"Select 2 for Subract\n"
"Select 3 for Mutiplication\n"
"Select 4 for Division\n"
"Select 5 for percentage\n"
"Select 6 for Sin value\n"
" Select 7 for cos value\n"
"Select 8 for Tan value \n"
"Select 9 for 1/x  value\n"
"Select 10 for arcsin\n"
"Select 11 for arccos\n"
"Select 12 for arc\n"
"Select 13 for log\n"
"Select 14 for sqrure\n"
"Select 15 for root\n "
"Select 16 for factorial\n"
"Select 17 for nPr \n"
"Select 18 for nCr \n"
"Select 19 for antilog\n"
"Select 20 for average \n")
n=int(input("Enter the number:"))
if(n==1):
    a=float(input("Enter the number:"))
    b=float(input("Enter the number:"))
    c=a+b
    print(c)
elif(n==2):
    a=float(input("Enter the number:"))
    b=float(input("Enter the number:"))
    c=a-b
    print(c)
elif(n==3):
    a=float(input("Enter the number:"))
    b=float(input("Enter the number:"))
    c=a/b
    print(c)
elif(n==4):
    a=float(input("Enter the number:"))
    b=float(input("Enter the number:"))
    c=a*b
    print(c)
elif(n==5):
    a=float
    (input("Enter the  value:"))
    b=float(input("Enter the total number:"))
    c=(a/b)*100
    print(c)    
elif(n==6):
    a=float(input("Enter the values in format of( 45 degree=pi/4=0.7853 , take here pi as 3.14)"))
    c=math.sin(a)
    print("sin value of  ",a,"is",c)
elif(n==7):
    a=float(input("Enter the values in format of( 45 degree=pi/4=0.7853 , take here pi as 3.14)"))
    c=math.cos(a)
    print("cos value of  ",a,"is",c)
elif(n==8):
    a=float(input("Enter the values in format of( 45 degree=pi/4=0.7853 , take here pi as 3.14)"))
    c=math.tan(a)
    print("tan value of  ",a,"is",c)
elif(n==9):
    a=int(input("Enter the number"))
    c=1/a
    print(c)
elif(n==10):
    a=int(input("Enter the value"))
    c=math.asin(a)
    print(c,"the answer in the format of ( example: 45 degree=pi/4=0.7853 , take here pi as 3.14)")
elif(n==11):
    a=int(input("Enter the value"))
    c=math.acos(a)
    print(c,"the answer in the format of ( example: 45 degree=pi/4=0.7853 , take here pi as 3.14)")
elif(n==12):
    a=int(input("Enter the value"))
    c=math.atan(a)
    print(c,"the answer in the format of ( example: 45 degree=pi/4=0.7853 , take here pi as 3.14)")
elif(n==13):
    a=float(input("Enter the value for (ln)"))
    c=math.log(a)
    print(c)
elif(n==14):
    a=float(input("Enter the number"))
    c=a*a
    print(c)
elif(n==15):
    a=float(input("Enter the number"))
    c=math.sqrt(a)
    print(c)
elif(n==16):
    num = int(input("Enter the number"))
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print("The factorial of",num,"is",factorial)
elif(n==17):
        print("Enter the Value of n: ")
        n = int(input())
        print("Enter the Value of r: ")
        r = int(input())

        fact = 1
        i = 1
        while i<=n:
          fact = i*fact
          i = i+1

        numerator = fact          
        sub = n - r              
        fact = 1
        i = 1
        while i<=sub:
          fact = i*fact
          i = i+1
        denominator = fact        
        perm = numerator/denominator

        print("\nPermutation =", perm)
elif(n==18):
    print("Enter the Value of n: ", end="")
    n = int(input())
    print("Enter the Value of r: ", end="")
    r = int(input())
    fact = i = 1
    while i<=n:
      fact = i*fact
      i += 1

    numerator = fact
    sub = n-r
    fact = i = 1

    while i<=sub:
      fact = i*fact
      i += 1

    denominator = fact
    
    fact = i = 1
    while i<=r:
      fact = i*fact
      i += 1

    denominator = fact*denominator
    comb = numerator/denominator
    print("\nCombination (nCr) =", comb)
elif(n==19):
    a=int(input("enter the number"))
    c=2.71828**(a)
    print(c)
elif(n==20):
    num = int(input('How many numbers: '))
    total_sum = 0
    for n in range(num):
        numbers = float(input('Enter number : '))
        total_sum += numbers
    avg = total_sum/num
    print('Average of ', num, ' numbers is :', avg)
else:
    print("Invaild input")
    print("try again with vaild input")
