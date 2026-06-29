def CheakDivisible(No):
	if(No % 3 == 0 and No % 5 ==0):
		return True
	else:
		return False

def main():

	print("Enter they number:")
	No = int(input())
	
	Ret = CheakDivisible(No)
	if(Ret):
		print("The Number is Divisible by 3 and 5")
	else:
		print("The Number is not divisible by 3 and 5")

if __name__ == "__main__":
	main()