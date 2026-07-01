Greater = lambda No1,No2 : No1>No2


def main():

	print("Enter the number...")
	No1 = int(input())
	print("Enter the second Number")
	No2 = int(input())
	
	
	Ret = Greater(No1,No2)
	if(Ret):
		print("No1 is greater than No2",Ret)
	else:
		print("No1 is smaller than No2",Ret)
	
if __name__ == "__main__":
	main()
