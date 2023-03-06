import random
import array

#intiate Variables

Length = int(input("Length = "))

Capital = int(input("Capital Characters = "))

Special = int(input("Special Characters = "))

Digits = int(input("Digital Numbers = "))

Low = Length - (Capital + Special + Digits)



#Generate Capaital Letters in List

Capital_letters = []

#Generate Capital

cap_ascii = 65
for i in range(26):
    Capital_letters.append(chr(cap_ascii))
    cap_ascii +=1

Capital_Character = random.sample(Capital_letters , Capital)

#Generate Lower

Lower_Char = []

lower_ascii = 97

for i in range(26):
    Lower_Char.append(chr(lower_ascii))
    lower_ascii+=1

Lower_Character = random.sample(Lower_Char , Low)


#Generate Special

Special_Char = []

special_ascii = 32

for i in range(7):
    Special_Char.append(chr(special_ascii))
    special_ascii+=1

Special_Character = random.sample(Special_Char , Special)


#Generate Digits

Digit_0 = []
Digit0 = 48

for i in range(10):
    Digit_0.append(chr(Digit0))
    Digit0+=1

Digit = random.sample(Digit_0 , Digits)

Password_List = Capital_Character + Lower_Character + Digit + Special_Character

Password = ''.join(map(str , Password_List))

#Print Password


print("Generated Password is" +" "+ Password)

