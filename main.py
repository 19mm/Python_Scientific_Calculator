print("Plz, select the type of Calculator:")
print("1.Standard\n2.Scientific")
choice=int(input("Enter your choice: "))
if choice==1:
    class cal():
        def add(self): 
            return a + b
        def sub(self):
            return a-b
        def multiply(self):
            return a*b
        def divide(self):
            return a / b
        def modulus(self):
            return a % b
        def floor(self):
            return a//b
    a = int(input('Enter First number : '))
    b = int(input('Enter Second number : ')) 
    obj=cal()
    while True :
        def menu():
            x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide \n5. Modulus\n6. Floor division') 
            print(x)
        menu()
        choice = int(input('Please select one of the following : '))
        if choice == 1:
            print("Addition is : ",obj.add())
        elif choice == 2:
            print("Substraction is: ",obj.sub())
        elif choice == 3:
            print("Multiplication is : ",obj.multiply()) 
        elif choice == 4:
            print("Division is : ",obj.divide())
        elif choice == 5:
            print("Remainder is : ",obj.modulus())
        elif choice == 6:
            print("Floor Division is : ",obj.floor())
        elif choice == 0:
            print('Again try one of the following')
        else:
            print('Invalid option')
            break
    print()

elif choice==2:
    import math
    class sci():         
        def ceilval(self):
            x=float(input("Enter a number: "))
            return math.ceil(x)
        def cosval(self):
            x=float(input("Enter a number: "))
            return math.cos(x)
        def sqrt(self):
            x=int(input("Enter a number: "))
            return math.sqrt(x)
        def rad(self):
            x=int(input("Enter a number: "))
            return math.radians(x)
        def power(self):
            x=int(input("Enter the base: "))
            y=int(input("Enter the power: "))
            return math.pow(x,y)
        def tanval(self):
            x=int(input("Enter a number: "))
            return math.tan(x)
        def rem(self):
            x=int(input("Enter dividend: "))
            y=int(input("Enter the divisor: "))
            return math.remainder(x,y)
        def sinval(self):
            x=int(input("Enter any Number:"))
            return math.sin(x)
        def fact(self):
            x=int(input("Enter a number: "))
            return math.factorial(x)
    obj=sci() 
    while True:    
        def menu1():
            x = ('1. Ceil \n2. Cos \n3. Square root \n4. Radian \n5. Power \n6. Tan \n7. Remainder \n8. Sin \n9. Factorial') 
            print(x)
        menu1() 
        choice = int(input('Please select one of the following : '))  
        if choice == 1:
            print("Ceil value is : ",obj.ceilval()) 
        elif choice == 2:
            print("Cos value is: ",obj.cosval())
        elif choice == 3:
            print("Square root is : ",obj.sqrt())
        elif choice == 4:
            print("Radian value is: ",obj.rad())
        elif choice == 5:
            print("Power value is: ",obj.power())
        elif choice == 6:
            print("Tan value is: ",obj.tanval())
        elif choice == 7:
            print("Reaminder value is: ",obj.rem())
        elif choice == 8:
            print("Sin value is: ",obj.sinval())
        elif choice==9 :
            print("Factorial of number is:",obj.fact())
        elif choice == 0:
            print('Again try one of the following')
        else:
            print('Invalid option')
            break    
    print()        






    
