CalculateSquare = lambda No : No * No


def main():
	print("Enter the number:")
	No = int(input())
	S = []
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	Ret = list(map(CalculateSquare,S))
	print("The Square will be :",Ret)
	

if __name__ == "__main__":	
	main()
