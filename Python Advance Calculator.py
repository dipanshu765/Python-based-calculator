def add_num(a,b):
    return a+b
def subs_num(a,b):
    return a-b
def mul_num(a,b):
    return a*b
def div_num(a,b):
    return a/b
def square(a):
    return (a**2)
def module(a,b):
    return a%b
def Fdivision(a,b):
    return a//b
def num_qube(a):
    return a*a*a
def fourthpower(a):
    return a*a*a*a
def findpower(a,b):
    return a**b
def factorial(num):
    return 1 if num==1 else (num*factorial(num-1))
def computeHCF(a, b):
    smaller = b if a > b else a  #consice way of writing if else statement
    hcf = 1
    for i in range(1, smaller+1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf
print("select option")
print('1.Addition')
print('2.Substraction')
print('3.multiplication')
print('4.division')
print('5.Modular Division')
print('6.Floar Division')
print('7.Find the Power')
print('8.Square')
print('9.Qube')
print('10.Power 4')
print('11.Factorial')

choice=int(input('enter a choice 1/2/3/4/5/6/7/8/9/10/11: '))
num1=float(input('enter a number:'))
if choice <8:
    num2=float(input('enter second number:'))

if choice==1:
    print('addition of {0} and {1} is {2}'.format(num1,num2, add_num(num1,num2)))
elif choice ==2:
    print('Substraction of {0} and {1} is {2}'.format(num1,num2, subs_num(num1,num2)))
elif choice ==3:
    print('Multiplication of {0} and {1} is {2}'.format(num1,num2, mul_num(num1,num2)))
elif choice ==4:
    print('Division of {0} and {1} is {2}'.format(num1,num2, div_num(num1,num2)))
elif choice==8:
    print('square of {0} is {1}'.format(num1,square(num1)))
elif choice==5:
    print('modular Division of {0} and {1} is {2}'.format(num1,num2,module(num1,num2)))
elif choice==6:
    print('floar division of {0} and {1} is {2}'.format(num1,num2,Fdivision(num1,num2)))
elif choice ==9:
    print('Qube of {0} is {1}'.format(num1,num_qube(num1)))
elif choice==10:
    print('Power 4 of the {0} is {1}'.format(num1,fourthpower(num1)))
elif choice==7:
    print('{0} power of {1} is {2}'.format(num1,num2,findpower(num1,num2)))
elif choice==11:
    print('factorial of {0} is {1}'.format(num1,factorial(num1)))
else:
    print('enter a valid choice')