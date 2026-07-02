CalculateFiveLetter = lambda No : len(No)>=5


def main():
	print("Enter the number:")
	No = int(input())
	S = list()
	for i in range(No):
		Num = (input())
		S.append(Num)
		
	fRet = list(filter(CalculateFiveLetter,S))
	print("The Minimum Number will be :",fRet)
	

if __name__ == "__main__":	
	main()
