from Arithematic import *

def main():

	print("Enter the first number..")
	iNo1 = int(input())

	print("Enter they Second Number...")
	iNo2 = int(input())
	
	iRet = Addition(iNo1,iNo2)
	print("Addition is :",iRet)
	
	iRet = Substraction(iNo1,iNo2)
	print("Substraction is :",iRet)
	
	iRet = Multiplication(iNo1,iNo2)
	print("Multiplication is :",iRet)
	
	iRet = Division(iNo1,iNo2)
	print("Division is :",iRet)
	
	
	
if __name__ == "__main__":
	main()