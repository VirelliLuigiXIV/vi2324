x = int(input("inserisci un numero composto dal tuo giorno e mese di nascita"
            + "(es. 02/10/2006, il numero è 210)"))
for num in range(x-25,x+25):
 if num % 3 == 0:
     print("Fizz",end="")
 if num % 5 == 0:
     print("Buzz",end="")
 if num % 14 == 0:
     print("AprilFish",end="")
 if num % 3 != 0 \
    and num % 5 != 0 \
    and num % 14 != 0:
     print(num,end="")
 print("")
     
