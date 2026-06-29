def PerfectNum(No):
	Sum = 0
	for i in range(1,No):
		if(No%i==0):
			Sum = Sum + i
			
			
			
	if(Sum == No):
		return True
		
	else:
		return False
			
def main():

	print("Enter they number:")
	No = int(input())
	
	Ret = PerfectNum(No)
	if(Ret):
		print("Given Number is perfect")
		
	else:
		print("Given Number is not Perfect")
	
if __name__ == "__main__":
	main()