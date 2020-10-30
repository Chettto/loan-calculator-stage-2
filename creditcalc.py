print('Enter the credit principal: ')
credit_principal = int(input())
print("""
What do you want to calculate?
type "m" - for count of months
type "p" - for monthly payment""")
calc = input()
if calc == 'm':
    print('Enter monthly payment:')
    monthly_payment = int(input())
    monthly = int(credit_principal / monthly_payment + 0.5)
    if monthly == 1:
        print('It will take ' + str(monthly) + ' month to repay the credit')
    else:
        print('It will take ' + str(monthly) + ' months to repay the credit')
elif calc == 'p':
    print('Enter count of months:')
    count_of_months = int(input())
    payment = - (-credit_principal // count_of_months)
    last_payment = credit_principal - (count_of_months - 1) * round(payment)
    if payment == last_payment:
        print('Your monthly payment = ' + str(payment))
    else:
        print('Your monthly payment = ' + str(payment) + ' with last month payment = ' + str(last_payment))
