# start = 1
# while start<=100:
#       if start%2==0:
#             print(start)
#       start+=1
# n=7
# sum = 0
# for i in range(1,n+1):
#       sum = sum+i
# print(sum)
# n=1
# sum=0
# while n<=100:
      
#       sum=sum+n
#       n+=1
      
# print(sum)
# while True:
#       ip_num = float(input('enter a number:'))
#       if ip_num<=0:
#             print('negative number')
#             break
# ip_num = float(input('enter a positive number:'))
# if ip_num<=0:
#       print('Negative number entered')
# while ip_num>0:
#       num_1 = float(input('enter a positive number'))
#       if num_1<=0:
#             print('negative number entered')
import random

# Define the snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initialize positions
# player_pos = [0, 0]  # player 1 and player 2

# def roll_dice():
#     return random.randint(1, 6)

# def move_player(player, pos):
#     dice = roll_dice()
#     print(f"Player {player + 1} rolled a {dice}")
#     pos += dice

#     if pos > 100:
#         print(f"Player {player + 1} needs exact roll to reach 100. Stay at {pos - dice}")
#         return pos - dice

#     if pos in snakes:
#         print(f"Oh no! Player {player + 1} got bitten by a snake at {pos}. Go to {snakes[pos]}")
#         pos = snakes[pos]
#     elif pos in ladders:
#         print(f"Yay! Player {player + 1} climbed a ladder from {pos} to {ladders[pos]}")
#         pos = ladders[pos]
#     else:
#         print(f"Player {player + 1} moved to {pos}")

#     return pos

# # Game loop
# turn = 0
# while True:
#     input(f"\nPlayer {turn + 1}, press Enter to roll the dice...")
#     player_pos[turn] = move_player(turn, player_pos[turn])

#     if player_pos[turn] == 100:
#         print(f"\n🎉 Player {turn + 1} wins the game! 🎉")
#         break

#     # Switch turn
#     turn = 1 - turn
# for class_no in range(1,11):
#       for roll_no in range(1,31):
#             if class_no%5 ==0 or roll_no<15:
#                   break
#             print(f'class_no {class_no} roll_no {roll_no}')
# def area_of_circle():
#       print('started printing area of the circle')
#       print(3.14*10*10)
#       print('finished printing area of the circle')
# area_of_circle()
# area_of_circle()
# area_of_circle()
 
# def table(num):
#       for i in range(1,11):
#             print(f'{num} x {i} = {num*i}')
# table(17)
# def sum_of_naturalnumbers(num1):
#       sum=0
#       for i in range(1,num1+1):
#             sum+=i
#       print(sum)
# sum_of_naturalnumbers(5)
# def multi_of_naturalnumbers(n):
#       mul = 1
#       for i in range(1,n+1):
#             mul*=i
#       print(mul)
# # multi_of_naturalnumbers(4)
# def simple_calculator(n1,n2,op):
#       while True:
#             n1=int(input('enter a number'))
#             n2=int(input('enter a number'))
#             op=input('enter a operation:').lower()
     
#       if op in ['+','add']:
#             print(n1+n2)
#       elif op in ['-','sub']:
#             print(n1-n2)
      
#       elif op in ['*','mul']:
#             print(n1*n2)
#       elif op in ['/','div']:
#             if n2!=0:
#                   print(n1/n2)
#       else:
#             print('invalid input')
#             break


      
# simple_calculator(2,3,'Add')
# def sum(a,b):
#       print(a,b)
# def sum(a,b,c):
#       print(a,b,c)
# def sum(a,b,c,d):
#       print(a,b,c,d)



# sum(1,2)
# sum(3,2,5)
# sum(3,4,3,5)


# def sum(a,*b):
#       temp = a
#       for i in b:
#             temp+=i
#       print(temp)

# sum(2,3)
# def test():
#     result = 10 > 5 and 3 < 1
#     return result or False
# print(test())
# def even_or_odd(n1):
      
#       if n1%2==0:
#             return 'even number'
#       else:
#             return 'odd number'
# resu= even_or_odd(3)
# print(resu)
# def simple_calculator(a,b):
#       return a+b, a-b,a*b,a/b
# r1= simple_calculator(2,3)
# print(r1)
# print(type(r1))



   




      

      

            

