def Square(No1):
	Ans = 1
	Ans = No1*No1
	
	return Ans


def main():
	
	print("Enter they number:")
	No = int(input())
	
	Ret = Square(No)
	print("Square of the given number is :",Ret)

if __name__ == "__main__":
	main()