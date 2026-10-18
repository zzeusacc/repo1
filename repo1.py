python.py
#task 1
a = int(input("enter a number"))
b = int(input("enter another number"))
if a > b:
print("a is greater than b")
elif b > a:
print("b is greater than a")
else:
print("numbers are equal")
#task 2
a = input("enter a number")
if a > 0:
print("the number is positive")
elif a < 0:
print("the number is negative")
else:
print("the number is equal to zero")
#task 3
a = int(input("enter a number"))
if a%2 == 0:
print("the number is even")
else:
print("the number is odd")
#task 4
a = int(input("enter your score"))
if a % 10 == 9 or a // 10 == 10:
if a > 100:
print("invalid score")
elif a == 90:
print("B")
else:
print("A")
elif a %1 0 == 8 or a % 10 == 9:
if a == 80:
print("C")
else:
    print("B")
elif a % 10 == 7 or a % 10 == 8:
if a == 70:
    print("D")
else:
    print("C")
elif a%10==5 or a%10==6:
    if a==60:
        print("E")
    else:
        print("D")
else:
print("F")
#task 5
a = input("enter a number")
b = input("enter a number")
c = input("enter a number")
if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
elif c > a and c > b:
    print("c is the largest number")
else:
    print("all numbers are equal")
#task 6
a = int(input("enter a number"))
b = int(input("enter a number"))
c = input("choose an operation")
d = ["+", "-", "*", "/", "**", "//"]
if c not in d:
    print("invalid operation")
else:
    print(f("{a} {c} {b}"))
#task 7
a = input("enter a number")
if a >= 0 and a <= 12:
    print("child")
elif a >= 13 and a <= 17:
    print("teenager")
elif a>==18 and a<==64:
    print("adult")
elif a > 64:
    print("senior")
else:
    print("invalid age")
#task 8
a = int(input("enter the total amount"))
if a < 100:
    print("no discount")
elif a>99 or a<300:
    print(a*10%)
elif a>299 or a<500:
    print(a*15%)
else:
    print(a*20%)
#task 9
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if a > b:
if a > c:
if b > c:
    print(c,b,a)
else:
    print(b,c,a)
else:
    print(b,a,c)
elif b>c:
    if a>c:
        print(c,a,b)
else:
    print(a,b,c)
#task 10
m = 1000
a = int(input("eded daxil edin"))
if a > m:
    print("invalid balance")
else:
    print(a, m-a)
#task 11
a = int(input("nece kWh?"))
if a >= 0 and a <= 100:
    print("0.08 AZN")
elif a>==101 and a<==300:
    print("0.12 AZN")
elif a>300:
    print("0.15 AZN")
#task 12
age = int(input("enter your age"))
salary = int(input("enter your salary"))
requested_loan = int(input("enter the requested loan"))
if age >= 18:
    if salary<==500:
        if requested_loan<==10:
            print("approved")
else:
    print("rejected")
else:
    print("rejected")
else:
    ("rejected")
#task 15
exam_score = int(input("enter the exam score"))
age=int(input("enter your age"))
school_score=int(input("enter your school score"))
if age > 15:
    if exam_score>==0 and exam_score<==700:
        if school_score>==0 and school_score<==100:
            if exam_score>==600:
                print("scolarship")
            elif exam_score>449 and exam_score<600:
                 print("accepted")
                elif exam_score>299 and exam_score<450 and school_score>79:
                     print("accepted")
    else:
        print("rejected, exam score is below 300")
        else:
            print("rejected,school score is invalid")
            else:
                print("rejected, exam score is invalid")
else:
print("rejected, your age is below 16")

