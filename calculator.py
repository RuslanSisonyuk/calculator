# calculator script
# 
# convert user inputed string into math function(s)
# possible algorithms:
# ----
# look for variable - operator pairs in highrearchy order, 
# grab the highest pair, calculate it and place the result back, modifying the string
# 5+4*6  9/4*4+8*2  9/(4*4)+8*2  9+(9+1)*(10+2)
			 						
# take string 9+((10+2*10)/(4+1))        
# search for (), take string inbetween () -> 10+2*10
# if no () in string, search for signs in order * / + -
# if operator exists, take numbers adjascent to it -> 2,10,*
# calculate equation and return result in place of the equation -> 10+20
# another operator exists in string, repeat calculation and return -> 30
#
#		calc(9 + calc( calc(calc(10 + 2*10) / calc(4+1) ))
# 			 9 +       ((   10 +    2*10     )     / (4+1))  
#	calc(initial equation):
#	while ( '(ec)' )   in.ec. + calc(ec.)
#	return solve ec.
#			20+10*8/2
#	solve(ec):
#	
import re

def solve_simple_eq(simple_equation,type):
	search_str1 = "\d+\{type}".format(type=type)
	search_str2 = "\{type}\d+".format(type=type)
	num1 = re.search(search_str1,simple_equation)
	num2 = re.search(search_str2,simple_equation)
	num1 = int(num1.group()[:len(num1.group())-1])
	num2 = int(num2.group()[1:])
	# print(num1)
	# print(num2)
	if(type=="*"): return str(num1 * num2)
	if(type=="/"): return str(int(num1 / num2))
	if(type=="+"): return str(num1 + num2)
	if(type=="-"): return str(num1 - num2)

def solve_eq(equation):
	while(re.search("[-\/\*\+]",equation)):
		if(re.search("\*",equation)):
			simple_equation = re.search("\d+\*\d+",equation).group()
			solved_eq = solve_simple_eq(simple_equation,"*")
			simple_equation = re.sub("\*","\\*",simple_equation)
			equation = re.sub(simple_equation,solved_eq,equation)
		elif(re.search("/",equation)):
			simple_equation = re.search("\d+/\d+",equation).group()
			solved_eq = solve_simple_eq(simple_equation,"/")
			#simple_equation = re.sub("/","/",simple_equation)
			equation = re.sub(simple_equation,solved_eq,equation)
		elif(re.search("-",equation)):
			simple_equation = re.search("\d+-\d+",equation).group()
			solved_eq = solve_simple_eq(simple_equation,"-")
			#simple_equation = re.sub("\-","\\-",simple_equation)
			equation = re.sub(simple_equation,solved_eq,equation)
		elif(re.search("\+",equation)):
			simple_equation = re.search("\d+\+\d+",equation).group()
			solved_eq = solve_simple_eq(simple_equation,"+")
			simple_equation = re.sub("\+","\\+",simple_equation)
			equation = re.sub(simple_equation,solved_eq,equation)

	return equation

def process_eq(equation):
	in_brackets = re.search("\(.*\)",equation)
	if(in_brackets):
		clean_in_brackets = in_brackets.group()[1:len(in_brackets.group())-1]
		equation = re.sub(in_brackets, process_eq(clean_in_brackets), equation)

	equation = solve(equation)
	return equation

def main():
	#process_eq("(12+(1+(11-1)))")
	print(solve_eq("10+8*20/10*2"))

	# test = "10+ 20*10 *10+10+23"
	# # print(re.search("\d+\*\d+",test))
	# test2 = re.sub("20\*10","\\*",test)
	# print(test2)


if __name__ == "__main__": 
	main()