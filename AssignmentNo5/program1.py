def CheakPrime(No):

	if No <=1:
		return False
	for i in range(2,No):
		if(No % i == 0):
			return False
		else:
			return True
	
	
	
		


def main():
	
	print("Enter the number:")
	No = int(input())
	
	Ret = CheakPrime(No)
	if(Ret):
		print("The Number is prime")
	else:
		print("The Number is not prime")

if __name__ == "__main__":
	main()