#IB910C -S VT2016 Laboration 1:
#Written in Python 2.7.9 using Mac OSX 10.3
import sys


#Determines Integer/Floating point division
def ret_datatype(input):
	if input == 'f' or input == 'F':
		return True
	elif input == 'i' or input == 'I':
		return False
	else:
		return -1
	
def main():
	try:
		#User specifies whether floating point or integer should be used
		is_float = ret_datatype(raw_input("Do you want to perform integer of float division? (Enter 'I' or 'F'): "))
		if is_float < 0:
			print "Invalid input specified, your options are i/I or f/F"
			sys.exit(-1)
		
		#Divisor and dividend are either typecast to integer or float
		if is_float:
			dividend = float(raw_input ("Enter dividend: "))
			divisor = float(raw_input ("Enter divisor: "))
		elif is_float == False:
			dividend = int(raw_input ("Enter dividend: "))
			divisor = int(raw_input ("Enter divisor: "))
		
		#Print computation
		print(str(dividend) + " / " + str(divisor) + " = " + str(dividend/divisor))
		
		
	except ValueError:
		print "Invalid value specified."
		sys.exit(-1)
		
	
	
	
if __name__ == "__main__":
    main()
