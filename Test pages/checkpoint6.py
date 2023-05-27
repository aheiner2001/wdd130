print("Rate from 1–10 on the following: ")

loan_size = int(input("How large is the loan?: "))

credit = int(input("How good is your credit history?: "))

income = int(input("How high is your income?: "))

downpayment = int(input("How large is your down payment?: "))

def yes():
    print("You have been acepted")
def no():
    print("You have not been acepted")

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        yes()
    elif credit >= 7 or income >=7:
        if downpayment >= 5:
            yes()
        else:
            no()
    else:
        no()
elif credit >= 4:
    if income >= 7 or downpayment >=7:
        yes()
    elif income >= 4 and downpayment >=4:
        yes()
    else:
        no()
else:
    no()        