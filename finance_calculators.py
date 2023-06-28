import math

print('**********INVESTMENT AND BOND CALCULATOR**********')
print('Investment - to calculate the amount of interest you\'ll earn on your investment')
print('Bond - to calculate the amount you\'ll have to pay on a home loan')


    #Check user input for correctness using while loop

while True:
    choice = input('Enter either "investment" or "bond" to proceed: ')
    if choice.lower() == 'investment' or choice.lower() == 'bond':
        break
    print('Invalid choice. Enter either investment or bond:')

    #Investment calculator based on the user choice

if choice.lower() == 'investment':
    deposit_amount = int(input('Enter deposit amount: '))
    interest_rate = float(input('Enter interest rate: '))
    years = int(input('Enter the number of years you plan to invest: '))
    interest_rate = interest_rate / 100
    
    #Check user input for correctness again

    while True:
        interest = input('Would you like simple or compound interest: ')
        if interest.lower() == 'simple' or interest.lower() == 'compound':
            break
        print('Enter either "simple" or "compound"')
        
    if interest.lower() == 'simple':
        total_amount = deposit_amount * (1 + interest_rate * years)
        print('The total amount is: £', + int(total_amount))
    else:
        total_amount = deposit_amount * math.pow((1 + interest_rate), years)
        print('The total amount is: £', + int(total_amount))


    #Bond calculator based on the user choice

else:

    house_value = int(input('Enter value of the house: '))
    interest_rate = float(input('Enter interest rate: '))
    time = int(input('How many months for repayment: '))

    interest_rate = (interest_rate / 100) / 12
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-time))
    print('Your monthly repayment is: £', + int(repayment))






