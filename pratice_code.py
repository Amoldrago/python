import math

#operator precedence and math functions
print("Math functions")
calculate = (2*3)*8+10*0.47
print("'round functionr' ->",round(calculate))
print("'comb functionr' ->",math.comb(5, 4))
print("'factorial functionr' ->",math.factorial(6))
print("\n")

print("'if' condition")
if(math.factorial(6)==720):
    print("Factorial function is working correctly")
else:
    print("Math is a blunder")
print("\n")

print("'for' loop")
for x in range(6):
  print(x*x+1)
print("\n")

price = 100000
good_cred = True
if good_cred:
    down_payment = 0.1*price
    print("You need to pay 10% down payment ")
    print("you need to pay",down_payment)
else:
    down_payment = 0.2*price
    print("You need to put 20% down payment")
    print("you need to pay", down_payment)