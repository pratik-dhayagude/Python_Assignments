def CalculateArea(No1,No2):
	Area=1;
	Area = No1*No2
	
	return Area


def main():

	print("Enter the length")
	No1 = int(input())
	print("Enter the weidth")
	No2 = int(input())
	
	Ret = CalculateArea(No1,No2)
	print("The Area will be:",Ret)
	
	
if __name__ == "__main__":
	main()