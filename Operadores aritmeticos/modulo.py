num=int(input("Introduzca el numero:"))


    
if num%2==0 and  num%3==0 and num%5==0:
    print("Director general")

elif num%3==0 and  num%5==0 and num%5!=0:
    print ("Directivo")

elif num%2==0 and  num%3!=0 and num%5!=0:
    print ("Staff")

elif num%2!=0 and  num%3!=0 and num%5!=0:
    print ("Seguridad")
