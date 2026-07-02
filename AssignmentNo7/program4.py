from functools import reduce

CalculateAddition = lambda No1,No2 : No1+No2


def main():
	print("Enter the number:")
	No = int(input())
	S = list()
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	fRet = (reduce(CalculateAddition,S))
	print("The Addition Numbers will be :",fRet)
	

if __name__ == "__main__":	
	main()
