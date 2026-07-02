CalculateEven = lambda No : No%2==1


def main():
	print("Enter the number:")
	No = int(input())
	S = []
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	fRet = list(filter(CalculateEven,S))
	print("The Odd Numbers will be :",fRet)
	

if __name__ == "__main__":	
	main()
