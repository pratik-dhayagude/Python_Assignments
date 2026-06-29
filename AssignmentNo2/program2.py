def CheakGreater(No1,No2):
	if(No1>No2):
		return No1 
		
		
	else:
		return No2
		
def main():
	
	print("Enter they first Number:")
	No1 = int(input())
	
	print("Enter the second number:")
	No2 = int(input()) 
	Ret = CheakGreater(No1,No2)
	if(Ret == True):
		print("No1 is Greater than No2:",Ret) 
	else:
		print("No2 is greater than No1:",Ret)
if __name__ == "__main__":

	main()