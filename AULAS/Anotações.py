frase = ('curso em video python')

# len = comprimento da frase, quantos blocos a frase está utilizando
print(len(frase))

#COUNT conta quantos " " tem na frase
frase.count('o')

#Diretrizes de analise de string :FATIAMENTO > (0:0:0) #(' ': 0 : 0) 

#Encontra o bloco em que se incia a string que procura = ex: find deo = bloco 11
#Se não encontrar retorna -1
print(frase.find('Z'))

print (frase.count('curso'))

# in funciona igualmente o Find, porem retorna o valor booleano, se existe ou não a palavra buscada
print('curso' in frase)

#Replace funciona para substituição, porém não sobrescreve a variável
#Caso queira que o Replace sobrescreva a variável, é preciso atribuir a variável novamente
#Ex: frase=frase.replace('Python', 'Android')

print(frase.replace('python', 'android'))

#Funções bastante usadas de transformação de string
#frase.upper() transforma a frase em maiúsculas
#frase.lower() transforma a frase em minúsculas
#frase.capitalize() capitaliza a frase (Atribuí maiúsculas no inicio do texto)
#frase.title() capitaliza a frase, porém em formato de titulo, todo inicio de palavra com letra maiúscula

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())


#TRANSFORMAÇÃO
#frase.strip() Remove espaços inúteis no inicio e no fim da frase
#também é possível utilizar a variação R/L direita ou esquerda para definir
#qual lado ele irá remover os espaços

print(('   CURSO EM VIDEO PYTHON  ').strip())

#DIVISÃO
#A função split() divide a frase pelo caractere definido, por padrão é o espaço
#você pode definir o caractere em que ele vai considerar a divisão dentro do parentese
# (' ') = ira dividir toda vez que encontrar espaço
# ('-') = ira dividir toda vez que encontra traço   
    #JUNÇÃO
    #Permite que você adicione algum caractere na frase que foi splitada

frasesplitada = frase.split()
print(frasesplitada[0])
print(frase.split()[0])

#Também é possível utilizar [] + [] para mostrar dentro de um split qual o bloco seguinte

print(frase.split()[2] [3])



