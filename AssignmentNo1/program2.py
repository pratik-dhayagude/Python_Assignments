def Factor(iNo):

	for i in range(1,iNo+1):
		if(iNo % i == 0):
			print(i)
			
		
		
	

def main():

	print("Enter they number")
	iNo = int(input())
	Factor(iNo)
	
if __name__ == "__main__":

	main()
