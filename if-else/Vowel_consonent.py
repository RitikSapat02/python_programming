a=input("Enter any character: ")
Vowel=(a=="a" or a=="A" or a=="e" or a=="E" or a=="i" or a=="I" or a=="o" or a=="O" or a=="u" or a=="U")

if(Vowel):
    print("Vowel")
elif(len(a)>1):
    print("Enter only one chracter")
else:
    print("Consonent")