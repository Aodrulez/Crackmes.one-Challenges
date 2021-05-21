import random

# URL: https://crackmes.one/crackme/606b1faf33c5d418e8c4009e
#
# [ Analysis of the Keygenme ] - Aodrulez (mr.atulalex@gmail.com)
# 1. The length of the serial has to be greater than 4 characters & less than 12
# 2. The length of the serial has to be an odd number (5, 7, 9, 11)
# 3. Let's assume the following example serial for further analysis: "1234567"
# 4. Only the characters at odd positions (1, 3, 5, 7) are actually used in calculation
#    by the validation routine.
# 5. The characters at even positions (2, 4, 6) determine the calculation used on 
#    characters at even positions.
# 6. This keygen follows the rule that if ascii code of characters at even positions 
#    are even values ('B'=66, 'D'=68 etc), then the validation routine simply 
#    subtracts ascii codes of characters at odd positions as follows:
#         5 - 7 = x
#         3 - x = y
#         1 - y = z
#    if (z == 0): 
#       Valid serial 
#    else:
#      Invalid serial


# [ Code ]
# Global variable(s)
generatedSerial = ""

def randomFiller():
    filler = 1
    while(filler % 2 == 1):
        filler = random.randint(48, 122)
    filler = chr(filler)
    return filler

def generateSerial(length=3):
    rangeVal = length-1
    values = []
    for x in range(0, rangeVal):
        if (x == 0):
            values.append(random.randint(48, 55))
            continue
        if (x == 1):
            i = random.randint(values[x-1]+60, 122)
            values.append(i)
            continue

        if (x == 2):
            first = values[x-2]
            second = values[x-1]
            i = random.randint(second-10, second-2)
            values.append(i)
            continue

        first = values[x-2]
        second = values[x-1]
        y = (first-second)
        if(y < 0):
            break
        i = random.randint(55, first-y)
        values.append(i)

    x = 0
    temp = 0
    while(x < rangeVal):
        if(x + 1 == rangeVal):
            break
        if(x == 0):
            temp = values[x+1]-values[x]
            x = x+1
            continue
        origTemp = temp
        temp = values[x+1]-temp
        x = x+1

    if ((len(values) != len(set(values))) or temp < 48 or temp == None):
        # Can be better, recurse!
        generateSerial(rangeVal+1)
    else:
        values.append(temp)
        global generatedSerial
        values.reverse()
        for x in values:
            generatedSerial = generatedSerial+chr(x)+randomFiller()
        generatedSerial = generatedSerial[:-1]

    if(generatedSerial.isalnum() == False):
        generatedSerial = ""
        generateSerial(rangeVal+1)


print("\n\t+------------------------------+")
print("\t|    Keygen for Sansuu (v2)    |")
print("\t+------------------------------+")
print("\t(c) Aodrulez\n")

try:
    randomSerialLength = random.randint(3, 6)
    generateSerial(randomSerialLength)
    randomSerialLength = randomSerialLength*2-1
    print(" [+] Random serial generated : "+generatedSerial +" (length="+str(randomSerialLength)+")\n\n")
except:
    print(" [-] Something went wrong, please try again.\n\n")