from time import sleep as s
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
encrypt=""
decrypt=""
print("Welcome Caesar Cipher encrypter & decrypter!")
act=str(input("(e)ncrypt or (d)ecrypt? "))
if act=='e':
	while True:
		try:
			msg=(input("enter the message:\n")).lower()
			key=int(input("enter the key:"))%26
			for i in msg:
				if i[0:1]==(" ") and len(i)>=1:
					encrypt+=i
				else:
					encrypt+=(alphabet[(key+alphabet.index(i))%26])				 
			print(encrypt)
			break	
		except ValueError:
			print("\nplease enter your message without any special charcters and key in only integer")
			s(3)

elif act=='d':
	while True:
                try:
                        msg1=(input("enter the message:\n")).lower()
                        key1=int(input("enter the key:"))%26
                        for i in msg1: 
                                if i[0:1]==(" ") and len(i)>=1:
                                        decrypt+=i
                                else:
                                        decrypt+=(alphabet[(alphabet.index(i)-key1)%26])
                        print(decrypt)
                        break 
                except ValueError:
                        print("\nplease enter your message without any special charcters and key in only integer")
                        s(3)

	
else:
	print("Wrong Para")
