Square = lambda No : No*No*No


def main():

	print("Enter the number...")
	No = int(input())
	
	Ret = Square(No)
	print("The Qube of the given number is:",Ret)
if __name__ == "__main__":
	main()
