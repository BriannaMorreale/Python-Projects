# Brianna Morreale
#CS1300
# 3/7/2022
# Word Calculator

# function to add the two number strings
def adder(st1, st2):
	
	check = None
	check2 = None
	
	# Used to check if the input is within the range 1-10
	allowed_nums = ["one", "two", "three", "four", "five",
					"six", "seven", "eight", "nine", "ten"]
	
	# All numbers and their numerical values				
	numbers = { "one" : 1,
				"two" : 2,
				"three" : 3,
				"four" : 4,
				"five" : 5,
				"six" : 6,
				"seven" : 7,
				"eight" : 8,
				"nine" : 9,
				"ten" : 10,
				"eleven" : 11,
				"twelve" : 12,
				"thirteen" : 13,
				"fourteen" : 14,
				"fifteen" : 15,
				"sixteen" : 16,
				"seventeen" : 17,
				"eighteen" : 18,
				"nineteen" : 19,
				"twenty" : 20,
				}
				
	print(f"Now adding {st1} and {st2} :")
	
	#Checks if the types are strings
	if(type(st1) == str and type(st2) == str):
		
		# Checks to see if the inputs are within the range
		for x in allowed_nums:
			if(st1 == x):
				check = st1
			if(st2 ==x):
				check2 = st2
		
		# If the input is 1-10 		
		if(check != None and check2 != None):	
			
			# Takes the two keys and adds the two values
			for k,v in numbers.items():
				if k == st1:
					var = v;
				if k == st2:
					var2 = v;
			answer = var+var2
			
			# Takes the result of the addition and prints the key
			for k, v in numbers.items():
				if v == answer:
					print(f"{k} \n")
		
		# If the number is smaller than 1 or bigger than 10			
		else:
			print("Please use the range one through ten.\n")

	# If the input is not a string	
	else:
		print("Please use the word, not the number.\n")
		
# The program uses a dictionary to find the word given and replace it
# with its numerical value. It then adds the two numbers and prints out
# the string word associated with the number. It also uses a list to 
# check to see if the input is a number 1 through 10.
