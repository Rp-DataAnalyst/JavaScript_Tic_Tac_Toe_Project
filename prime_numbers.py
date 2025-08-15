# num1 = int(input('enter a number:'))
# if num1== 0 or 1:
#       print('you entered a wrong number')
# else:
#       count=0
#       for i in range(1,num1+1):
#             if num1%i==0:
#                   count+=1
#       if count==2:
#             print('It is a prime number')
#       else:
#             print('It is a composite number')
# num1 = int(input('enter a number:'))
# if num1<=1:
#       print('not a prime number')
# else:
#        flag = True
#        for i in range(2,num1):
#               if num1%i ==0:
#                      flag == False
#                      print('not a prime number')
#                      break
# if flag == True:
#        print('It is a prime number')
# def check_prime(input_num):
#       if input_num<=1:
#             return('This is not a prime number')
#       for i in range(2,input_num):
#             if input_num%1==0:
#                   return 'This is not a prime number'
#             return 'This is a Prime number'
# print(check_prime(29))
# def check_prime(input_num):
#       if input_num<=1:
#             return('This is not a prime number')
#       for i in range(2,input_num//2+1):
#             if input_num%1==0:
#                   return 'This is not a prime number'
#             return 'This is a Prime number'
# print(check_prime(29))
# num1 = input('Enter a ticket number: ')

# Check if length is between 1 and 10
# if 1 <= len(num1) <= 10:
#     def check_palindrome(num1):
#         if num1 == num1[::-1]:  # Reverse check
#             print('Lucky Ticket')
#         else:
#             print('It is not a lucky ticket')

#     check_palindrome(num1)
# else:

#     print('Ticket number length must be between 1 and 10 digits')
n = int(input('enter a number:'))

if 1 <= n <= 10**4:
    total = 0
    for i in range(1, n + 1):
        total += i**2
    print(total)
else:
    print("Invalid input")




                  

 
      
