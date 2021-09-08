#preste bem a atenção: esse tipo de algoritmo usa de conjuntos (set!)
# sendo assim, sua sintaxe é: 'set()', ele pode ser adicionado por '.add', e podemos verificar
# se ele está contido em outro elemento pode meio do 'A.issubset(B)'

palavra = 'ferreiro'
print('Advinhe qual é a palavra: ')
for i in palavra:
    print('_', end = ' ')
print()

palavra_set = set(palavra)
tentativas = set()
chances = 6

#O loop vai acontecer até que todas as letras digitadas façam parte da palavra
while not palavra_set.issubset(tentativas):
    print('Letras já digitadas: ', end=' ')
    print('/ '.join(tentativas))
    print()
    print(f'Número de tentativas: {chances}')
    letra = input('Digite uma letra: ')
    tentativas.add(letra)
    print()
    print('A palavra é: ', end = ' ')

#buscar dentro da variável palavra para cada letra, caso esteja dentro do conjunto tentativas, imprimir a letra.
    for i in palavra:
        if i in tentativas:
            print(i, end = ' ')
        else:
            print('_', end = ' ')
    print()

# Verificar se a letra digitada faz parte da palavra a ser adivinhada
    if letra in palavra:
        print('Acertou!')
    else:
        chances -= 1
        if chances > 0:
            print(f'Errado! Você pode tentar de novo  (Chances: {chances})')
        else:
            print('Acabaram as suas chances! Tente outra vez')
            break
    print()
