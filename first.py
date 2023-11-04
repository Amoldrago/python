print("hello")


print("Load approval")
price = input("Enter the load amount you are looking for ")
cred_score = input("Enter your current cred score ")
cred = int(cred_score)
if cred < 600:
    down_payment = 0.5*float(price)
    print("Your cred score is below average, so you need to pay below amount")
    print(down_payment)
elif cred>600 and cred<700:
    down_payment = 0.2*float(price)
    print("Your cred score is good, so you need to pay below amount")
    print(down_payment)
else:
    down_payment = 0.1*float(price)
    print("Your cred score is excellent, so you need to pay below amount")
    print(down_payment)
