CheakEven = lambda No :(No%5==0)


def main():

	print("Enter the number...")
	No = int(input())
	
	
	
	Ret = CheakEven(No)
	if(Ret):
		print("It is Divisible by 5")
	else:
		print("It is Not Divisible by 5")
	
if __name__ == "__main__":
	main()
