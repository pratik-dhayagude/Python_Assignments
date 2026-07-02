from functools import reduce

CalculateMaximum = lambda No1,No2 : No1 if No1>No2 else No2


def main():
	print("Enter the number:")
	No = int(input())
	S = list()
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	fRet = (reduce(CalculateMaximum,S))
	print("The Maximum Number will be :",fRet)
	

if __name__ == "__main__":	
	main()
