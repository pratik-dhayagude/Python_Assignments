CheakEven = lambda No :(No%2==0)


def main():

	print("Enter the number...")
	No = int(input())
	
	
	
	Ret = CheakEven(No)
	if(Ret):
		print("It is Even Number")
	else:
		print("It is Odd number")
	
if __name__ == "__main__":
	main()
