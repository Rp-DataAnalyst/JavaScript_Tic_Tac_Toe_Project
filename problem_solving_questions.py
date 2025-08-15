# def check_given_number(num1):
#       if num1>0:
#             return('The given number is a positive number')
#       elif num1==0:
#             return('The given number is a zero')
#       else:
#             return('The given number is a negative number')
# input_num1=int(input('enter a number'))
# res = check_given_number(input_num1)
# print(res)


# def check_number_status(num):
#       if num>0:
#             print('the given number is a positive number')
#       else:
#             if num==0:
#                   print('the given number is a zero')
#             else:
#                   print('the given number is a negative number')
# input_num = int(input('enter a nmber'))
# check_number_status(input_num)
# def even_or_odd(num1):
#       if num1%2==0:
#             print('Given number is a even number')
#       else:
#             print('Given number is a odd number')
# input_number=int(input('enter a number'))
# even_or_odd(input_number)
# def check_voter_eligibility_status(age):
#       if age>=18:
#             print('This person is eligible to vote')
#       else:
#             print('This person is a minor')
# input_age=int(input('enter your age'))
# check_voter_eligibility_status(input_age)
# Solving problem using ternary operator
# def even_or_odd(num1):
#       res= 'even' if num1%2==0 else 'odd'
#       print(res)
# even_or_odd(23)
# def check_voting_eligibility(age):
#       res = 'eligible to vote' if age>=18 else 'He is a minor'
#       print(res)
# check_voting_eligibility(99)
def greatest_of_two_numbers(num1,num2):
      return num1 if num1>num2 else num2

res=greatest_of_two_numbers(233,45)
print(res)


