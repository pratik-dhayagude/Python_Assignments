CalculateEven = lambda No : No%2==0


def main():
	print("Enter the number:")
	No = int(input())
	S = []
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	fRet = list(filter(CalculateEven,S))
	print("The Even Numbers will be :",fRet)
	

if __name__ == "__main__":	
	main()
