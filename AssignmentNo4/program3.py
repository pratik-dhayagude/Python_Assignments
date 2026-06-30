def Factorial(No):
	Sum = 1
	
	for i in range(1,No+1):
		Sum = Sum*i
		
	return Sum

def main():

	
	print("Enter the number")
	No = int(input())
	Ret = Factorial(No)
	print("Factorial of the given number is:",Ret)
if __name__ == "__main__":
	main()