"""
Ask the user for a number. Depending on whether the number 
is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
"""

x = int(input("Enter a number: "))
y = (x % 2)
if y == 0:
	print("The number even!")
else:
	print("The number is odd!")


	
