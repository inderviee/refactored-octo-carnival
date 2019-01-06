#Your Name
#Functions

# All function definitions must include:
#   a contract
#   a purpose statement
#   appropriate one test cases.

#
WAGE_PER_HOUR = 12
TAX_RATE = .15

################################################################################
# Problem 1
# Utopia's tax accountants always use programs that compute income taxes even 
# though the tax rate is a solid, never-changing 15%. Define the functions 
# gross_pay, tax, and net_pay.
# Assume an hourly wage of $12 and a tax rate of 15%.


# gross_pay: number -> number
# Purpose: consumes number of hours works and produces the gross pay earned.
# Note: wage is $12 per hour
def gross_pay(hrs):
    return hrs * WAGE_PER_HOUR

#test cases for gross_pay

# tax: number -> number
# Purpose: consumes gross pay earned and produce amount of tax owed.
# Note: tax rate is 15%
def tax(pay):
    return pay * TAX_RATE

#test cases for tax

# net_pay: number -> number
# Purpose: consumes the number of hours worked and produces amount earned after
#          taxes are paid
def net_pay(hrs):
    return gross_pay(hrs) - tax(gross_pay(hrs))

#test cases for net_pay
print net_pay(10)
################################################################################
# Problem 2
# The local supermarket needs a program that can compute the value of a 
# bag of coins. Define the function sum_coins. It consumes four numbers: 
# the number of pennies, nickels, dimes, and quarters in the bag; 
# it produces the amount of money in the bag.

#Contract: write me
#Purpose: write me
def sum_coins(p, n, d, q):
    pass # write me

#test cases write me


################################################################################
# Problem 3
# An old-style movie theater has a simple profit function. 
# Each customer pays $5 per ticket. 
# Every performance costs the theater $20, plus $.50 per attendee. 
# Develop the function total_profit. 
# It consumes the number of attendees (of a show) and 
# produces how much income the attendees produce.

#write it all, contract, purpose, function, test cases