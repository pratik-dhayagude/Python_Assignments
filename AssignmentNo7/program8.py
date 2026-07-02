DivisibleByFiveAndThree = lambda No :(No%3==0)and(No%5==0)


def main():
	print("Enter the number:")
	No = int(input())
	S = list()
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	fRet = list(filter(DivisibleByFiveAndThree ,S))
	print("The Number will be :",fRet)
	

if __name__ == "__main__":	
	main()
