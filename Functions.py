# # # # # Function is a block of code which can be executed whenever you want
# # # # # def area_of_triangle(b,h):
# # # # #       area = 1/2*b*h
# # # # #       print(area)
# # # # # area_of_triangle(4,5)
# # # # def calculator(a,b):
# # # #       print(a+b)
# # # #       print(a-b)
# # # #       print(a*b)
# # # #       if b!=0:
# # # #             print(a/b)
      
# # # #             print(a%b)
# # # #             print(a//b)
# # # #       else: 
# # # #             print('Division by zero is not possible')
# # # #       print(a**8)
      
            
# # # # calculator(4,8)
# # # # def Table_Printer(num1):
# # # #       for i in range(1,21):
# # # #             print(num1,'x',i,'=', num1*i)

# # # # Table_Printer(20)
# # # #sum of n natural numbers
# # # def factorial_numbers(n):
# # #       factorial = 1
# # #       for i in range(1,n+1):
# # #             factorial*=i
# # #       print (factorial)

# # # factorial_numbers(6)
# # #Keyword Arguments
# # def simple_calculator(num1, num2=10):
# #       print("a+b=", num1+num2)


# # simple_calculator(5,10)
# # #Default Arguments 
# # simple_calculator(5)
# # #Error:1 Postitional argument is following keyword argument
# # #Error:2 Parameter without a dafault is following parameter with a default
# def sum(a,*b):
#       temp = a
#       for i in b:
#             temp=temp+i
#       print(temp)


# # def sum(a,b,c):
# #       print(a+b+c)


# # def sum(a,b,c,d):
# #       print(a+b+c+d)


# sum(2,3)
# sum(4,5,6)
# sum(5,7,8,9)

