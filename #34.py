#STATEMENT ON EXERCISE
# Make a code that asks an employee's salary and calculates their increase:
#CONDITIONS:
#For a salary higher than R$ 1.250,00: Increase 10%.
#For a salary lower/equal than R$ 1.250,00: Increase 15%

N = float(input('Digite seu salário atual: '))


if N > 1250:
    print('Seu novo salário é: {:.2f}'.format(N*1.10))
else:
    print('Seu novo salário é: {:.2f}'.format(N*1.15))
