def DisplayReverse(iNo):
	while(iNo > 0):
		print(iNo)
		iNo = iNo-1
	
		


def main():
	print("Enter they number...")
	iNo = int(input())
	
	DisplayReverse(iNo)

if __name__ == "__main__":
	main()