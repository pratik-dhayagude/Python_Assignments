def CheakEven(No):
	if(No %2 ==0):
		return True
	else:
		return False

def main():

	print("Enter the number:")
	No =  int(input())
	Ret = CheakEven(No)
	if(Ret):
		print("Number is even")
	else:
		print("Number is odd")
if __name__ == "__main__":
	main()