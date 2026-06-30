def CountDigit(No):
	Temp = 0
	Digit = No
	while(No!=0):
		Digit  = No %10
		Temp = Temp *10+Digit
		No = No//10
		
		
	return Temp 


def main():
	
	print("Enter they Number")
	No = int(input())
	
	Ret = CountDigit(No)
	
	print("Reverse Number is:",Ret)

if __name__ == "__main__":
	main()