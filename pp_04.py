"""
Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides 
evenly into another number. For example, 13 is a divisor of 
26 because 26 / 13 has no remainder.)
"""

#The run time calculation was not required for this problem.
import time
start, end = 0, 0
start = time.time()
#-----------------------------------
user = int(input("Enter a number: "))

x = user
new = []

while x >= 1:
	if user % x == 0:
		new.append(x)
	x -= 1

print(new)
#-----------------------------------

end = time.time()
print(end - start)
