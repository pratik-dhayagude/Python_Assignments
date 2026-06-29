def CalculateRadius(Radius):
	ans = 1
	ans = 3.14 * Radius * Radius
	
	return ans

def main():
	print("Enter the area of circle :")
	Radius = int(input())
	
	Ret = CalculateRadius(Radius)
	print("the radius of the circle is:",Ret)
	
	

if __name__ == "__main__":
	main()