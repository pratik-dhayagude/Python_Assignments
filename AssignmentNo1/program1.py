def CheakVowel(Character):

	if(Character == "A" or Character == "a" or
	   Character == "E" or Character == "e" or
	   Character == "I" or Character == "i" or 
	   Character == "O"or Character == "o" or 
	   Character == "U" or Character == "u"):
		return True
	else:
		return False


def main():
	
	Character = input("Enter they character....")
	
	bRet = CheakVowel(Character)
	
	if(bRet == True):
		print("This is Vowel")
	else:
		print("This is not a Vowel")
	



if __name__ == "__main__":
	main()