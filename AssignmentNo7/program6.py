from functools import reduce

CalculateMinimum = lambda No1,No2 : No1 if No1<No2 else No2


def main():
	print("Enter the number:")
	No = int(input())
	S = list()
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	fRet = (reduce(CalculateMinimum,S))
	print("The Minimum Number will be :",fRet)
	

if __name__ == "__main__":	
	main()
