#your name here
#Test Cases

#average : number number -> number
#Computes the average of two numbers.
def average(a, b):
    avg = (a + b) / 2
    return avg

#Insert test case for printing the average of 2 and 6
print(average(2,6))

################################################################################
#C2F : number -> number
#Converts a Celsius temperature into Fahrenheit.
def C2F(tempC):
    tempF = (tempC * 9/5) + 32
    return tempF

 
#Insert test case for converting 0 degrees celsius
#Insert test case for converting 100 degrees celsius

#print (C2F(0))
#print (C2F(100))
################################################################################
# tooLong : string -> boolean
# Determines whether a password has more than 8 characters.
def tooLong(word):
    if len(word) > 8:
        return True
    else:
        return False

#Insert test case for "foo"
#Insert test case for "whatever"
#Insert test case for "impossible"
print tooLong("Foo")
print tooLong("whatever")
print tooLong("impossible")
################################################################################
#translateNum : number -> string
#Translates a small number into Spanish.
def translateNum(num):
    if num == 1:
        return "uno"
    elif num == 2:
        return "dos"
    elif num == 3:
        return "tres"
    elif num == 5:
        return "cinco"
    elif num == 8:
        return "ocho"

 
#Insert appropriate test cases
print translateNum(5)
print translateNum(2)
print translateNum(1)
################################################################################
#graduating : number -> string
#Consumes a YOG, produces the name of the class graduating that year
def graduating (year):
    if year == 2019:
        return "senior"
    elif year == 2020:
        return "junior"
    elif year == 2021:
        return "sophomore"
    elif year == 2022:
        return "freshman"
    else:
        return"Unknown"


#Insert test case for 2006
#Insert test case for your YOG (if you have one!)
print graduating(2006)
print graduating(2022)
################################################################################
#ticketCost : number -> number
#Computes the price of a given number of movie tickets.
#Tickets cost $9 each for 9 or fewer, $7 each for 10 or more.
def ticketCost(num_tickets):
    if num_tickets < 10:
        return num_tickets * 9
    if num_tickets < 0:
        return = 0
    else:
        return num_tickets * 7

   
 

#Insert test cases for ticketCost
#Challenge: this code is hackable, find it and fix it.

print ticketCost(5)
print ticketCost(9)
print ticketCost(2)
print ticketCost(-5)