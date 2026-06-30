def CountDigit(No):
	Sum = 0
	Digit = No
	while(No!=0):
		Digit  = No %10
		Sum = Sum+Digit
		No = No//10
	return Sum


def main():
	
	print("Enter they Number")
	No = int(input())
	
	Ret = CountDigit(No)
	
	print("The Sum is:",Ret)

if __name__ == "__main__":
	main()