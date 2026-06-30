def SumNatural(No):
	Sum = 0
	
	for i in range(0, No+1):
		Sum = Sum+i
		
	return Sum
	


def main():

	print("Enter the number")
	No = int(input())
	Ret = SumNatural(No)
	print("The sum of the natural number :",Ret)
if __name__ == "__main__":
	main()