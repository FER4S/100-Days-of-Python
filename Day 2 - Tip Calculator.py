print('Welcome to the tip calculator.')
totalBill=float(input("What was the total bill? $"))
tipPercentage=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
peopleNum=int(input("How many people to split the bill? "))

tipPercentage/=100
tipPercentage+=1
print(f'{tipPercentage=}')
eachPerson=(totalBill/peopleNum)*tipPercentage
print(f'Each person should pay: ${round(eachPerson,2):.2f}')