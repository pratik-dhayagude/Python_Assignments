CheakEven = lambda No :(No%2==1)


def main():

	print("Enter the number...")
	No = int(input())
	
	
	
	Ret = CheakEven(No)
	if(Ret):
		print("It is odd Number")
	else:
		print("It is Even number")
	
if __name__ == "__main__":
	main()
