def CountDigit(No):
	Temp = 0
	Digit = No
	while(No != 0):
		Digit  = No % 10
		Temp = Temp * 10 + Digit
		No = No//10
		
	if(Temp == No):
		return True
	else:
		return False
		
		
	
		

def main():
	
	print("Enter they Number")
	No = int(input())
	
	Ret = CountDigit(No)
	if(Ret):
		print("The given number is palindrm Number")
	else:
		print("The number is not palindrom Number")

if __name__ == "__main__":
	main()