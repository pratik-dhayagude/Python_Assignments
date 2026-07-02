from functools import reduce

CalculateProduct = lambda No1,No2 : No1*No2


def main():
	print("Enter the number:")
	No = int(input())
	S = list()
	for i in range(No):
		Num = int(input())
		S.append(Num)
		
	fRet = (reduce(CalculateProduct,S))
	print("The Product Numbers will be :",fRet)
	

if __name__ == "__main__":	
	main()
