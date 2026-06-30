def CountDigit(No):
	Count=0
	Digit = No
	while(No!=0):
		Digit  = No %10
		Count = Count+1
		No = No//10
	return Count


def main():
	
	print("Enter they Number")
	No = int(input())
	
	Ret = CountDigit(No)
	
	print("The Count is:",Ret)

if __name__ == "__main__":
	main()