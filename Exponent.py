print("2^3 = " + str(2**3))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print("---Welcome to the EXPONENT EXPERIENCE---")
base = int(input("Please enter the base number to be raised: "))
exponent = int(input("Please enter the exponent of the base number: "))





print("Your result is: " + str(base) +"^"+str(exponent) + " = "+str(raise_to_power(base,exponent)))