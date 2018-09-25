'''
done
'''
suatuInteger = 1985
print(suatuInteger , " bertipe " , type(suatuInteger))

jadiString = str(suatuInteger)
print(jadiString , " bertipe " , type(jadiString))

stringJadiInt = int(jadiString)
print(stringJadiInt , " bertipe " , type(stringJadiInt))

benarSalah = False #coba ganti jadi True
print(benarSalah , " bertipe " , type(benarSalah))

booleanJadiString = str(benarSalah)
print(booleanJadiString , " bertipe " , type(booleanJadiString))

stringJadiBoolean = booleanJadiString == "True"
print(stringJadiBoolean , " bertipe " , type(stringJadiBoolean))