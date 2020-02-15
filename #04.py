ALGO = input('Digite algo: ')

print('{} | Qual tipo primitivo? R: {} ' .format(ALGO, type(ALGO)))
print('{} | Só tem espaços?      R: {} ' .format(ALGO, ALGO.isspace()))
print('{} | É um numero?         R: {} ' .format(ALGO, ALGO.isnumeric()))
print('{} | É alfabético?        R: {} ' .format(ALGO, ALGO.isalpha()))
print('{} | É alfanumérico?      R: {} ' .format(ALGO, ALGO.isalnum()))
print('{} | Está em maiusculo?   R: {} ' .format(ALGO, ALGO.isupper()))
print('{} | Está em minusculo?   R: {} ' .format(ALGO, ALGO.islower()))
print('{} | Está Capitalizado?   R: {} ' .format(ALGO, ALGO.istitle()))

