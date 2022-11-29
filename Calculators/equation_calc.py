# Brianna Morreale
# CS1300
# 3/7/2022
# Equation Calculator

# Substrings that will be checked when the user types their equation
add = "+"
subtract = "-"
multiply = "*"
divide = "/"
b = True

# Intro. to the calculator
print("\nWelcome to the Equation Calculator.")
print("Please type a number, an operator, and a number.")
print("Operators are: +, -, *, and /")

# Loops to let the user keep adding equations
while(b == True):
	try:
		print("\nType 'exit' to exit.")
		eq = input("Please enter the equation: \n")
		
		# If the user wants to exit
		if eq.lower() == "exit":
			print("Goodbye.\n")
			b = not b

		# If the user's equation is addition
		elif add in eq:
			if eq.count("+") == 1:
				sp = eq.split("+")
				answer = int(sp[0]) + int(sp[1])
				print(f"{sp[0]} + {sp[1]} = {answer}")
			else:
				print("Please only use two numbers and one operator.")
		
		# If the user's equation is subtraction	
		elif subtract in eq:
			if eq.count("-") == 1:
				sp2 = eq.split("-")
				answer2 = int(sp2[0]) - int(sp2[1])
				print(f"{sp2[0]} - {sp2[1]} = {answer2}")
			else:
				print("Please only use two numbers and one operator.")
		
		# If the user's equation is multiplication	
		elif multiply in eq:
			if eq.count("*") == 1:
				sp3 = eq.split("*")
				answer3 = int(sp3[0]) * int(sp3[1])
				print(f"{sp3[0]} * {sp3[1]} = {answer3}")
			else:
				print("Please only use two numbers and one operator.")
			
		
		# If the user's equation is division	
		elif divide in eq:
			if eq.count("/") == 1:
				sp4 = eq.split("/")
				answer4 = int(sp4[0]) / int(sp4[1])
				print(f"{sp4[0]} / {sp4[1]} = {answer4}")
			else:
				print("Please only use two numbers and one operator.")
		
		# If the user uses words for any part of the equation
		else:
			print("Invalid. Please use the number, not the word.")
			print("Also, please type the operator as: +, - , *, /\n")
	
	#If the user uses more than 2 numbers
	except ValueError:
		print("Incorrect formatting.")
		print("Please only use two numbers.")
		
	
		
# The progam begins by introducing the calculator to them and asking 
# them for an equation. It also lets them know they can exit by typing
# "exit". Then, it takes the string and looks for one of the substrings.
# Then it splits the string at the operator and converts the two objects
# on the left and right into integers. Then, it performs the operation 
# and prints out the equation and answer. There are messages in case the
# user uses more than 2 numbers, uses words, or any other formatting 
# issues. They will be able to redo their equation. 
